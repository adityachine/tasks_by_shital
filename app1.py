import streamlit as st
import pandas as pd
import io
import openai

# Set API key from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

st.set_page_config(page_title="AI Excel Filter", layout="wide")

st.title("🧠 Excel Filter Automation with Agentic AI")
st.write("Upload two Excel files, enter your filter instruction, and let AI do the rest!")

# Upload Excel Files
file1 = st.file_uploader("📂 Upload Inputfile1.xlsx", type="xlsx")
file2 = st.file_uploader("📂 Upload Inputfile2.xlsx", type="xlsx")

# User Prompt
user_instruction = st.text_input("💬 Enter filter instruction")

def load_excel(file):
    return pd.read_excel(file)

if file1 and file2 and user_instruction:
    df1 = load_excel(file1)
    df2 = load_excel(file2)

    schema = f"""
You have two DataFrames: 'df1' and 'df2'.
df1 columns: {', '.join(df1.columns)}
df2 columns: {', '.join(df2.columns)}

Instruction from user:
{user_instruction}

Write Python pandas code to create:
- filtered_df1
- filtered_df2
"""

    with st.spinner("🤖 Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes pandas code."},
                    {"role": "user", "content": schema}
                ],
                temperature=0.2,
            )

            code = response.choices[0].message["content"]
            st.subheader("🧾 AI-Generated Filtering Code")
            st.code(code, language="python")

            local_vars = {"df1": df1.copy(), "df2": df2.copy(), "pd": pd}
            exec(code, {}, local_vars)

            filtered_df1 = local_vars.get("filtered_df1")
            filtered_df2 = local_vars.get("filtered_df2")

            if filtered_df1 is not None and filtered_df2 is not None:
                merged_df = pd.concat([filtered_df1, filtered_df2], ignore_index=True)

                st.subheader("✅ Filtered DataFrame 1")
                st.dataframe(filtered_df1)

                st.subheader("✅ Filtered DataFrame 2")
                st.dataframe(filtered_df2)

                st.subheader("🔗 Merged DataFrame")
                st.dataframe(merged_df)

                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    filtered_df1.to_excel(writer, sheet_name="Filtered_df1", index=False)
                    filtered_df2.to_excel(writer, sheet_name="Filtered_df2", index=False)
                    merged_df.to_excel(writer, sheet_name="Merged", index=False)

                st.download_button("📥 Download Excel", output.getvalue(), "Filtered_Output.xlsx")

            else:
                st.error("❌ AI did not return the expected variable names.")

        except Exception as e:
            st.error(f"⚠️ Error executing AI-generated code: {e}")

import streamlit as st
import pandas as pd
import io
import requests
import json

# Hugging Face API config
HUGGINGFACE_API_KEY = st.secrets["huggingface"]["api_key"]
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Content-Type": "application/json"
}

def query_huggingface(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.2,
            "max_new_tokens": 400
        }
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    result = response.json()
    return result[0]['generated_text'] if isinstance(result, list) else str(result)

def load_excel(file):
    return pd.read_excel(file)

# Streamlit app layout
st.set_page_config(page_title="AI Excel Filter (Hugging Face)", layout="wide")
st.title("🤖 Excel Filter Automation with Hugging Face AI")
st.write("Step-by-step filter automation using conversational AI.")

# File upload & instruction
file1 = st.file_uploader("📂 Upload Inputfile1.xlsx", type="xlsx")
file2 = st.file_uploader("📂 Upload Inputfile2.xlsx", type="xlsx")
user_instruction = st.text_input("💬 Enter your filter instruction")

# Extra options
merge_option = st.checkbox("🔗 Merge filtered DataFrames", value=True)
output_file_name = st.text_input("📁 Enter output Excel file name", value="Filtered_Output.xlsx")

# Once all required inputs are available
if file1 and file2 and user_instruction:
    df1 = load_excel(file1)
    df2 = load_excel(file2)

    schema = f"""
You have two pandas DataFrames: df1 and df2.
df1 columns: {', '.join(df1.columns)}
df2 columns: {', '.join(df2.columns)}

User instruction:
{user_instruction}

Write Python pandas code to filter:
- filtered_df1
- filtered_df2
Only output the code.
"""

    with st.spinner("🧠 Hugging Face AI is generating pandas filtering code..."):
        try:
            code = query_huggingface(schema)
            st.success("✅ Code generated successfully!")

            # Display code
            st.subheader("🧾 AI-Generated Code")
            st.code(code, language="python")

            # Ask user to confirm before executing
            run_code = st.button("▶️ Run this code")

            if run_code:
                local_vars = {"df1": df1.copy(), "df2": df2.copy(), "pd": pd}
                try:
                    exec(code, {}, local_vars)
                    filtered_df1 = local_vars.get("filtered_df1")
                    filtered_df2 = local_vars.get("filtered_df2")

                    if filtered_df1 is not None and filtered_df2 is not None:
                        st.success("✅ Code executed successfully!")
                        st.subheader("📊 Filtered DataFrame 1")
                        st.dataframe(filtered_df1)

                        st.subheader("📊 Filtered DataFrame 2")
                        st.dataframe(filtered_df2)

                        # Optionally merge
                        if merge_option:
                            merged_df = pd.concat([filtered_df1, filtered_df2], ignore_index=True)
                            st.subheader("🔗 Merged DataFrame")
                            st.dataframe(merged_df)
                        else:
                            merged_df = None

                        # Download section
                        output = io.BytesIO()
                        with pd.ExcelWriter(output, engine='openpyxl') as writer:
                            filtered_df1.to_excel(writer, sheet_name="Filtered_df1", index=False)
                            filtered_df2.to_excel(writer, sheet_name="Filtered_df2", index=False)
                            if merged_df is not None:
                                merged_df.to_excel(writer, sheet_name="Merged", index=False)

                        st.download_button("📥 Download Excel", output.getvalue(), file_name=output_file_name)

                    else:
                        st.error("❌ Expected 'filtered_df1' and 'filtered_df2' not found in AI code.")

                except Exception as ex:
                    st.error(f"⚠️ Error while executing code: {ex}")

        except Exception as e:
            st.error(f"❌ Hugging Face API error: {e}")

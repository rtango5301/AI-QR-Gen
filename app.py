import streamlit as st
import replicate


@st.cache_data
def generating_image(prompt, url):
    output = replicate.run(
        "nateraw/qrcode-stable-diffusion:9cdabf8f8a991351960c7ce2105de2909514b40bd27ac202dba57935b07d29d4",
        input={
            "seed": 1234,
            "prompt": prompt,
            "strength": 0.9,
            "batch_size": 1,
            "guidance_scale": 7.5,
            "negative_prompt": "ugly, disfigured, low quality, blurry, nsfw",
            "qr_code_content": url,
            "num_inference_steps": 40,
            "controlnet_conditioning_scale": 1.5
        }
    )
    return output[0]

def main():
    st.set_page_config(page_title="AI QR Code Generator")
    st.title("AI QR Code Generator")

    # Create input fields
    prompt = st.text_input("Enter Prompt", "")
    url = st.text_input("Enter URL", "")

    # Submit button
    if st.button("Submit"):
        if prompt and url:
            output = generating_image(prompt, url)
            st.image(output, caption="Generated QR Code", use_column_width=True)
        else:
            st.error("Please fill in both fields.")
    
    # Download button
    if 'output' in locals() and output:
        href = f'<a href="{output}" download="qr_code.png">Download QR Code</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
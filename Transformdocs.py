import streamlit as st
from streamlit_option_menu import option_menu
import pdfplumber
import json
import xml.etree.ElementTree as ET
import os
import pandas as pd 

# Setting up page layout and title
st.set_page_config(page_title="TransformODocs", layout="wide")
query_params = st.query_params
page = query_params.get("page", "main")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/streamlit_css.css")


st.markdown("""
    <style>
        /* Navbar container */
        .navbar {
            display: flex;
            justify-content: space-between;
            background-color: #0e1117;
            padding: 15px;
            border-radius: 10px;
        }

        /* Navbar brand */
        .navbar .brand {
            color: #fff;
            font-size: 24px;
            text-decoration: none;
        }

        /* Navbar links */
        .navbar .nav-links {
            display: flex;
            gap: 15px;
        }

        .navbar .nav-links a {
            color: #fff;
            font-size: 18px;
            text-decoration: none;
            padding: 10px 15px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }

        .navbar .nav-links a:hover {
            background-color: #575757;
        }

        /* Navbar login button */
        .navbar .login-btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .navbar .login-btn:hover {
            background-color: #45a049;
        }

        /* Center the title */
        .title {
            font-size: 32px;
            text-align: center;
            margin-top: 40px;
            color: #fff;
        }

        /* Subtitle */
        .subtitle {
            font-size: 24px;
            text-align: center;
            margin-bottom: 40px;
            color: #ddd;
        }

        /* Conversion boxes */
        .conversion-option {
            text-align: center;
            background-color: #444;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
        }

        .conversion-option h2 {
            font-size: 20px;
            color: #fff;
        }

        .conversion-option img {
            width: 50px;
            margin-bottom: 10px;
        }

        .conversion-option p {
            font-size: 16px;
            color: #ccc;
        }
    </style>
""", unsafe_allow_html=True)


if page == "main":
# Navigation Bar
    st.markdown("""
        <div class="navbar">
            <a class="brand" href="#">TransformODocs</a>
            <div class="nav-links">
                <a href="#">Home</a>
                <a href="#">Services</a>
                <a href="#">About Us</a>
                <a href="#">Contact Us</a>
            </div>
            <button class="login-btn">Login</button>
        </div>
    """, unsafe_allow_html=True)



    # Custom CSS to style the page (you can modify this as needed)
    st.markdown("""
        <style>
            .title {
                font-size: 32px;
                text-align: center;
                margin-bottom: 20px;
                color: #fff;
            }
            .subtitle {
                font-size: 24px;
                text-align: center;
                margin-bottom: 40px;
                color: #fff;
            }
            .conversion-option {
                text-align: center;
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 22px;
                box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
            }
            .conversion-option h2 {
                font-size: 20px;
                color: #000;
            }
            .conversion-option img {
                width: 50px;
                margin-bottom: 10px;
            }
            .conversion-option p {
                font-size: 16px;
                color: #555;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title and subtitle
    st.markdown("<div class='title'>Transform Your Business with AI-Powered Document Automation</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>TransformoDocs: Your All-in-One Document Solution Convert, Extract and Store with Ease, Seamless, and Powerful.</div>", unsafe_allow_html=True)

    
    # Display conversion options
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="conversion-option">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c9/JSON_vector_logo.svg" alt="JSON">
                <div class="card-title">JSON</div>
                <div class="card-text">Make your Docs files machine readable by converting them into a JSON file.</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html = True)
        c1,c2,c3 = st.columns((1,2,1))
        with c2:
            if st.button("Convert to JSON"):
                st.query_params = {"page": "json"}
                




    # Example usage



    with col2:
        st.markdown("""
            <div class="conversion-option">
                <img src="https://www.seekpng.com/png/detail/335-3353598_png-file-svg-file-csv-icon-png.png" alt="CSV">
                <div class="card-title">CSV</div>
                <div class="card-text">Make your Docs files machine readable by converting them into a CSV file.</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html = True)
        c1,c2,c3 = st.columns((1,2,1))
        with c2:
            if st.button("Convert to CSV"):
                st.query_params = {"page": "csv"}
    with col3:
        st.markdown("""
            <div class="conversion-option">
                <img src="https://img.icons8.com/?size=100&id=103741&format=png&color=000000" alt="XML">  
                <div class="card-title">XML</div>
                <div class="card-text">Make your Docs files machine readable by converting them into an XML file.</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html = True)
        c1,c2,c3 = st.columns((1,2,1))
        with c2:
            if st.button("Convert to XML"):
                 st.query_params = {"page": "xml"}
    # Optional: Add login button or any additional functionality at the top-right
    #st.sidebar.button("Login", key="login")

elif page == "json":
    # JSON Upload Page
    st.markdown("<h1>Upload your file to Convert to JSON</h1>", unsafe_allow_html=True)
    
    left_col,cen_col,right_col = st.columns((1,2,1))
    with cen_col:
        uploaded_file = st.file_uploader("Choose a file to convert to JSON")
        def pdf_to_json(pdf_path, json_path):
            # Initialize an empty dictionary to hold PDF data
            pdf_data = {}

            # Open the PDF file
            with pdfplumber.open(pdf_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    # Extract text from the current page
                    page_text = page.extract_text()
                    pdf_data[f"Page_{i+1}"] = page_text

            # Write the extracted data to a JSON file
            with open(json_path, 'w') as json_file:
                json.dump(pdf_data, json_file, indent=4)

            return json_path
        
        if uploaded_file is not None:
            # Handle the file upload and conversion here
            
            st.write("File uploaded successfully!")
            json_path = "output.json"  # Path to save the JSON file
            pdf_to_json(uploaded_file, json_path)
        
            with open(json_path, 'r') as json_file:
                json_content = json_file.read()

        # Display a download button after processing
            st.download_button(label="Download JSON", data=json_content, file_name="output.json", mime="application/json")
        if st.button("Go back"):
            st.query_params = {"page": "main"}
            
            
            
elif page == "xml":      
    st.markdown("<h1>Upload your file to Convert to XML</h1>", unsafe_allow_html=True)
    
    left_col,cen_col,right_col = st.columns((1,2,1))
    with cen_col:
        pdf_path = st.file_uploader("Choose a file to convert to XML")   
            
        def pdf_to_xml(pdf_path, xml_path):
            # Initialize the root of the XML tree
            root = ET.Element("Document")

            # Open the PDF file
            with pdfplumber.open(pdf_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    # Extract text from the current page
                    page_text = page.extract_text()

                    # Create an XML element for this page
                    page_element = ET.SubElement(root, "Page", number=str(i + 1))
                    # Add the text to the page element
                    text_element = ET.SubElement(page_element, "Text")
                    text_element.text = page_text

            # Create a tree structure with the root element
            tree = ET.ElementTree(root)

            # Write the tree to an XML file
            with open(xml_path, "wb") as xml_file:
                tree.write(xml_file, encoding="utf-8", xml_declaration=True)

            return xml_path
    
        if pdf_path is not None:
            # Handle the file upload and conversion here
            
            st.write("File uploaded successfully!")
            xml_path = "output.xml"  # Path to save the JSON file
            pdf_to_xml(pdf_path, xml_path)
        
            with open(xml_path, 'r') as xml_file:
                xml_content = xml_file.read()

        # Display a download button after processing
            st.download_button(label="Download JSON", data=xml_content, file_name="output.xml", mime="application/xml")
        if st.button("Go back"):
            st.query_params = {"page": "main"}
            
elif page == "csv":
    st.markdown("<h1>Upload your file to Convert to CSV</h1>", unsafe_allow_html=True)
    left_col,cen_col,right_col = st.columns((1,2,1))
    with cen_col:
        

        def pdf_to_csv(pdf_file, csv_file):
    # Initialize a list to hold data from all pages
            all_pages = []

            # Open the PDF file
            with pdfplumber.open(pdf_file) as pdf:
                for i, page in enumerate(pdf.pages):
                    # Extract table data from the current page (assuming the PDF contains tables)
                    table = page.extract_table()

                    if table is not None:
                        # Convert the table data into a pandas DataFrame
                        df = pd.DataFrame(table)

                        # Append the page's table DataFrame to the list of all pages
                        all_pages.append(df)

            # Concatenate all DataFrames from all pages
            if all_pages:
                final_df = pd.concat(all_pages, ignore_index=True)

                # Save the concatenated DataFrame to a CSV file
                final_df.to_csv(csv_file, index=False)
                return csv_file
            else:
                return -1
                
        pdf_file = st.file_uploader("Choose a file to convert to csv")
        
        if pdf_file is not None:
            st.write("File uploaded successfully!")
            csv_file = "output.csv"  # Path to save the CSV file
            result = pdf_to_csv(pdf_file, csv_file)
            st.write(result)

            if result != -1:
        # Reading the content of the CSV file to prepare it for download
                with open(csv_file, 'r') as csv_fl:
                    csv_content = csv_fl.read()
                st.download_button(label="Download CSV", data=csv_content, file_name="output.csv", mime="text/csv")
            else:
                st.write("Pdf file has no numerical data")
        if st.button("Go back"):
            st.query_params = {"page": "main"}

    

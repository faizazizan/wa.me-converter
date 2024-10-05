import streamlit as st

# Function to clean and convert a phone number to WhatsApp format
def convert_to_whatsapp(number):
    # Remove any '+', spaces, or '-'
    number = number.replace('+', '').replace(' ', '').replace('-', '')
    # Ensure the number starts with '0' and remove it, replace with country code '60'
    if number.startswith('0'):
        number = '60' + number[1:]
    return f"wa.me/{number}"

# Streamlit app interface
st.title('Bulk WhatsApp Number Converter')
st.write('Convert multiple Malaysian phone numbers to WhatsApp link format.')

# Input for phone numbers (multiline text)
phone_numbers = st.text_area('Enter your phone numbers, one per line (e.g., 0123456789):')

if st.button('Convert'):
    if phone_numbers:
        # Split the input into individual phone numbers
        numbers_list = phone_numbers.splitlines()
        whatsapp_links = [convert_to_whatsapp(number.strip()) for number in numbers_list if number.strip()]
        
        if whatsapp_links:
            st.success('Converted WhatsApp links:')
            # Display the links in a text area for easy copying without formatting
            st.text_area('Converted Links:', '\n'.join(whatsapp_links), height=200)
        else:
            st.error('Please enter at least one valid phone number.')
    else:
        st.error('Please enter valid phone numbers.')

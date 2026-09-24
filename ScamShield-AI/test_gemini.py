from gemini_service import analyze_message


message = """
URGENT! Your bank account will be blocked today.
Complete your KYC immediately using this link.
"""


result = analyze_message(message)

print(result)
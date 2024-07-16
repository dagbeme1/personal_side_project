#!/usr/bin/env python3

import http.client  # Import the HTTP client library to make HTTP requests
import json  # Import the JSON module to handle JSON data

def ask_question(query):
    conn = http.client.HTTPSConnection("chatgpt-gpt4-ai-chatbot.p.rapidapi.com")  # Create an HTTPS connection to the RapidAPI endpoint

    payload = json.dumps({"query": query})  # Convert the query to JSON format

    headers = {
        'x-rapidapi-key': "24151f6615mshc6617e1401be309p1201d5jsn032cd299a78f",  # RapidAPI key for authentication
        'x-rapidapi-host': "chatgpt-gpt4-ai-chatbot.p.rapidapi.com",  # RapidAPI host for the endpoint
        'Content-Type': "application/json"  # Content type in the request header
    }

    conn.request("POST", "/ask", payload, headers)  # Make a POST request to /ask with payload and headers

    res = conn.getresponse()  # Get the HTTP response object
    data = res.read()  # Read the response data
    conn.close()  # Close the HTTP connection

    return data.decode("utf-8")  # Decode the response data from bytes to string

def main():
    exit_commands = {"exit", "close", "end", "stop", "quit", "bye"}  # Set of commands to exit the chatbot
    print("Welcome to Blackbox! How can I help you with your health today? Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")  # Prompt user for input
        if user_input.lower() in exit_commands:  # Check if user wants to exit
            print("Blackbox: Goodbye!")
            break  # Exit the while loop
        response = ask_question(user_input)  # Get response from the chatbot API
        print(f"Blackbox: {response}")  # Print the chatbot's response

if __name__ == "__main__":
    main()  # Start the main function if this script is run directly

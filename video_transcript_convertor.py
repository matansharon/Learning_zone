import os
import anthropic

def get_anthropic_response(text):
    
    client=anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"))
    message = client.messages.create(
            # model="claude-3-opus-20240229",
            model='claude-3-haiku-20240307',
            max_tokens=4000,
            temperature=0.2,
            system=f"""
            the user input is a video transcript of a lecture.
            summarize the transcript.
            and then add a python code that demonstrate to concept of the lecture.
            """,
            messages=[
                {"role": "user", "content":text}
            ]
        )



def main():
    file_name=input("Enter the name of the output file: ")
    if file_name:
        text=""
        with open("transcript.txt") as f:
            text=f.read()
        res=get_anthropic_response(text)
        with open(file_name+".txt","w") as f:
            f.write(res)










if __name__ == '__main__':
    main()
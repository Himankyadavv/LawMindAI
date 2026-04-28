# main.py

from dotenv import load_dotenv
load_dotenv()

from crew import legat_assistant_crew


def run(user_input: str):
    result = legat_assistant_crew.kickoff(inputs={"user_input": user_input})

    print("_" * 50)
    print(result)
    print("-" * 50)


if __name__ == "__main__":
    user_input = (
        "A man broke into my house at night while my family was sleeping. "
        "He stole jewelry and cash from our bedroom. When I confronted him, "
        "he threatened me with a knife and ran away. We reported it to the police, "
        "but I'm not sure which legal charges should be filed under IPC."
    )

    run(user_input)

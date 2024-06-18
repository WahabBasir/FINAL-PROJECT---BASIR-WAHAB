print('BASIR P. WAHAB')
print('1BSCE-B')
print()
print('ICT 09 Programming 1')
print('FINAL PROJECT')
print()
print('PYTHON PROJECT 3 - TYPING MASTER')
print()
print()

import time

def main():
    text = "The quick brown fox jumps over the lazy dog."
    
    print("Welcome to Typing Master!")
    print("=========================")
    input("Press Enter to start typing the following text:\n{}\n".format(text))
    
    start_time = time.time()
    
    user_input = input("Start typing:\n")
    
    end_time = time.time()
    typing_time = end_time - start_time
    
    correct_chars = 0
    for i in range(min(len(text), len(user_input))):
        if text[i] == user_input[i]:
            correct_chars += 1
    
    accuracy = (correct_chars / len(text)) * 100
    
    print("\n\n----- Typing Results -----")
    print("Time taken: {:.2f} seconds".format(typing_time))
    print("Accuracy: {:.2f}%".format(accuracy))
    
    if accuracy == 100:
        print("Congratulations! Perfect typing!")
    elif accuracy >= 90:
        print("Great job! Your typing accuracy is excellent.")
    elif accuracy >= 80:
        print("Good effort! You have a decent typing accuracy.")
    else:
        print("Keep practicing. Improve your typing accuracy.")
    
if __name__ == "__main__":
    main()
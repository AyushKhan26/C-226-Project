from pynput.keyboard import Key,Listener
import datetime

refsent= 'An Ethical hacker is a skilled professional who has excellent technical knowledge and skill and know how to exploit vulnerabilities in target systems.He works with the permission of the owners of the system. An ethical hacker must comply with the rules of the target organization or owner and law of the land and their aim is to assess the security posture of a target organization/system '
print('\n\nType this sentence below to check your typing speed!')
print('\n\n',refsent,'\n\n')

correct,incorrrect = 0,
current_index = 0

start_time = datetime.datetime.now()

def on_press(key):
   global correct,incorrrect,current_index,start_time,refsent 

   if key == Key.shift:
      pass  
   else :
      if key == Key.backspace and current_index >0:
          current_index -= 1
      elif key == Key.backspace:
          pass
      elif str(key).replace("'","") == refsent[current_index] or (key == Key.space and refsent[current_index] == ' '):
          correct += 1
          current_index +=1 
      else :
          incorrrect +=1
          current_index +=1
     
def on_release(key):
    global refsent,correct,incorrrect,current_index,start_time

    if current_index >= len(refsent):
        totaltime = datetime.datetime.now() - start_time
        accuracy = (correct * 100)/(correct + incorrrect)
        print(f"Total time taken {totaltime} and accuracy is {accuracy}")
        return False
    

with Listener(on_press=on_press,on_release= on_release) as listener:
     listener.join()
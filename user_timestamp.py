from nlp import *
from datetime import time
from beg_sentence import *
import string
########################################################################################
# math helpers                                                                         #   
########################################################################################
def count_results(json):
    count = 0
    for i in json.results:
        count += 1
    return count

def count_words(result):
    count = 0
    for i in result.alternatives[0].words:
        count += 1
    return count

def in_range_time(pin_time, start_time, end_time):
    if pin_time <= end_time and pin_time >= start_time:
        return True
    return False

########################################################################################
# funcs                                                                                #   
########################################################################################

def search_for_proper(sentence, entity_dict):
    sent = sentence.split(" ")
    tags = set()
    # print(sent)
    for word in sent:
        if word == "":
            continue
        if word[-1] == ".":
            word = word[:-1]
        for key in entity_dict:
            if key.lower() == word.lower():
                for tag in entity_dict[key][0]:
                    tags.add(tag)
    return tags
# print(search_for_proper("Hi im a hi.", {"hi": [["hi", "hi"],1] , "im":[["me"],1],}))

# TODO: num appears

# based on pinned time, searches for word 
def find_start_end_time(json, time):
    response = json

    res_count = count_results(response)
    print(res_count)
    for j in range(res_count):
        # print("\n\n\n")
        # print("\t\t" + str(time))

        # print(result.alternatives[0].words[0], result.alternatives[0].words[-1])

        result = response.results[j]
        start_t = result.alternatives[0].words[0].start_time
        if j == res_count - 1:
            end_t = result.alternatives[0].words[-1].end_time
        else:
            end_t = response.results[j+1].alternatives[0].words[0].start_time
        
        if in_range_time(time, start_t, end_t):

            count = count_words(result)
            for i in range(count):
                word_start = result.alternatives[0].words[i].start_time
                if i == count - 1:
                    word_end = result.alternatives[0].words[i].end_time
                else:
                    word_end = result.alternatives[0].words[i+1].start_time
                if in_range_time(time, word_start, word_end):
                    return (result.alternatives[0].words[i].word, 
                            result.alternatives[0].words[i].start_time, 
                            result.alternatives[0].words[i].end_time,
                            result.alternatives[0].words[i])
    
                    

def process_timestamp(json, time):
    response = json

    pin_word, start_t, end_t, word_object = find_start_end_time(json, time)
    if pin_word == start_t == end_t == word_object == 0:
        print("pinned something before they even said something you fucking idiot")
        return
    beg_word, beg_start, beg_end, sentence = get_beg_sentence(response, word_object)
    topics_response, entities = topics()
    entity_dict = entity_filter_search(entities, topics_response)
    tags = search_for_proper(sentence, entity_dict)
    return tags
    





def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# # Test array 
# arr = [ 2, 3, 4, 10, 40 ] 
# x = 10
  
# # Function call 
# result = binary_search(arr, 0, len(arr)-1, x) 
  
# if result != -1: 
#     print("Element is present at index", str(result)) 
# else: 
#     print("Element is not present in array") 
def get_beg_sentence(json, beg_word):
    response = json

    start_time = beg_word.start_time
    end_time = beg_word.end_time
    beg_start = 0
    beg_end = 0
    sentence = ""

    #TODO: nanos edge case
    for result in response.results:
        #test cases
        
        count = 0
        for word in result.alternatives[0].words:
            count += 1
        flag = False
        for i in range(count):
            cur_entry = result.alternatives[0].words[i]
            if cur_entry.start_time == start_time and cur_entry.word == beg_word.word and cur_entry.end_time == end_time:
                cur = i
                while (not flag):
                    cur -= 1
                    if cur == -1:
                        flag = True
                    if result.alternatives[0].words[cur].word[-1] == '.':
                        flag = True

                cur += 1
                entry = result.alternatives[0].words[cur]
                beg_word = entry.word
                beg_start = entry.start_time
                beg_end = entry.end_time
                while entry.word[-1] != '.':
                    sentence = sentence + " " + entry.word
                    cur = cur + 1
                    entry = result.alternatives[0].words[cur]
                sentence = sentence + " " + entry.word

                break
        if flag:
            break

    return (beg_word, beg_start, beg_end, sentence)


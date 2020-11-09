
import sys
#TODO: nanos edge case

def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""


    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="en-US",
        audio_channel_count=2,
        model="video",
        enable_word_time_offsets=True,
        enable_automatic_punctuation=True,
        use_enhanced=True,
        diarization_config=speech.SpeakerDiarizationConfig(
            enable_speaker_diarization=True,
            min_speaker_count=4,
            max_speaker_count=4,
        )
        
    )

    operation = client.long_running_recognize(
        request={"config": config, "audio": audio}
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=1000)

    
    with open('full-json.txt', 'w') as f:
        print(response, file=f)

    fulltext = ""

    # beg_word = response.results[1].alternatives[0].words[7]

    # start_time = beg_word.start_time
    # end_time = beg_word.end_time
    # print(start_time)
    # print(end_time)
    # beg_start = 0
    # beg_end = 0

    # #TODO: nanos edge case
    # for result in response.results:
    #     #test cases
        
    #     count = 0
    #     for word in result.alternatives[0].words:
    #         count += 1
    #     flag = False
    #     for i in range(count):
    #         cur_entry = result.alternatives[0].words[i]
    #         print(cur_entry)
    #         print(beg_word)
    #         if sameTime(cur_entry.start_time, start_time) and cur_entry.word == beg_word.word and sameTime(cur_entry.end_time, end_time):
    #             print('hello')
    #             cur = i
    #             while (not flag):
    #                 cur -= 1
    #                 if cur == -1:
    #                     flag = True
    #                 if result.alternatives[0].words[cur].word[-1] == '.':
    #                     flag = True
    #             entry = result.alternatives[0].words[cur + 1]
    #             beg_word = entry.word
    #             beg_start = entry.start_time
    #             beg_end = entry.end_time

    #             break
    #     if flag:
    #         break

    # print(beg_word)
    # print(beg_start)
    # print(beg_end)

    

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        fulltext += result.alternatives[0].transcript
        fulltext += "\n\n"
        print("Confidence: {}".format(result.alternatives[0].confidence))

    with open('full-output.txt', 'w') as f:
        print(fulltext, file=f)

    speaker_tags = response.results[-1]
    with open('full-speakers.txt', 'w') as f:
        curr_speaker = 0
        prev_speaker = speaker_tags.alternatives[0].words[0].speaker_tag
        curr_block = ""
        blocks = []
        for words in speaker_tags.alternatives[0].words:
            curr_speaker = words.speaker_tag
            if curr_speaker != prev_speaker:
                
                blocks.append(curr_block)
                print("\n" + str(prev_speaker), file=f)
                prev_speaker = curr_speaker
                print(curr_block, file=f)
                curr_block = ""
            curr_block = curr_block + " " + words.word
        print("\n" + str(curr_speaker), file=f)
        print(curr_block, file=f)

    return response




                

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




response = transcribe_gcs("gs://kt38/trimmed-daily.flac")
beg_word = response.results[1].alternatives[0].words[9]


print(get_beg_sentence(response, beg_word))
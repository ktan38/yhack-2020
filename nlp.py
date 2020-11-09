import sys
import meaningcloud

# @param model str - Name of the model to use. Example: "IAB_en" by default = "IPTC_en"
model = 'IAB_en'

# @param license_key - Your license key (found in the subscription section in https://www.meaningcloud.com/developer/)
license_key = 'f0f682f46f2e1a814b4a53cd92888447'

# @param text - Text to use for different API calls
text = 'London is a very nice city but I also love Madrid.'

document = 'full-output.txt'


try:
    # We are going to make a request to the Topics Extraction API
    topics_response = meaningcloud.TopicsResponse(meaningcloud.TopicsRequest(license_key, doc=document, lang='en',
                                                                             topicType='e').sendReq())

    # If there are no errors in the request, we print the output
    if topics_response.isSuccessful():
        print("\nThe request to 'Topics Extraction' finished successfully!\n")

        entities = topics_response.getEntities()
        if entities:
            print("\tEntities detected (" + str(len(entities)) + "):\n")
            for entity in entities:
                print("\t\t" + topics_response.getTopicForm(entity) + ' --> ' +
                      topics_response.getTypeLastNode(topics_response.getOntoType(entity)) + "\n")

        else:
            print("\tNo entities detected!\n")
    else:
        if topics_response.getResponse() is None:
            print("\nOh no! The request sent did not return a Json\n")
        else:
            print("\nOh no! There was the following error: " + topics_response.getStatusMsg() + "\n")


    formatted_categories = ''

    deepcat_response = meaningcloud.DeepCategorizationResponse(meaningcloud.DeepCategorizationRequest(license_key, model=model, doc= document).sendReq())


    if deepcat_response.isSuccessful():
        categories = deepcat_response.getCategories()
        if categories:
            print("\tCategories detected (" + str(len(categories)) + "):\n")
            for cat in categories:
                print("\t\t" + deepcat_response.getCategoryLabel(cat) + ' --> ' +
                      deepcat_response.getCategoryRelevance(cat) + "\n")
        else:
            print("\tNo categories detected!\n")
    else:
        print("\tOops! Request to Deep Categorization was not succesful: (" + deepcat_response.getStatusCode() + ') ' + deepcat_response.getStatusMsg())


    summary = ''
    print("\tGetting automatic summarization...")
    summarization_response = meaningcloud.SummarizationResponse(meaningcloud.SummarizationRequest(license_key, sentences=4, doc = document).sendReq())
   
   
    if summarization_response.isSuccessful():
        summary = summarization_response.getSummary()
        print(summary)
    else:
        print("\tOops! Request to Summarization was not succesful: (" + summarization_response.getStatusCode() + ') ' + summarization_response.getStatusMsg())

except ValueError:
    e = sys.exc_info()[0]
    print("\nException: " + str(e))
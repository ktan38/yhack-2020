import sys
import meaningcloud

# @param model str - Name of the model to use. Example: "IAB_en" by default = "IPTC_en"
model = 'IAB_en'

# @param license_key - Your license key (found in the subscription section in https://www.meaningcloud.com/developer/)
license_key = 'f0f682f46f2e1a814b4a53cd92888447'

# @param text - Text to use for different API calls
text = 'London is a very nice city but I also love Madrid.'

document = 'full-output.txt'

def entity_filter_tags(entities, topics_response):
    entity_dict = dict()
    for entity in entities:
        topic = topics_response.getTopicForm(entity)
        ontology = topics_response.getOntoType(entity)
        num_appear = topics_response.getNumberOfAppearances(entity)
        tags_list = ontology.split(">")

        # remove "Top"
        if len(tags_list) > 1:
            tags_list = tags_list[1:]
        
        if topic in entity_dict.keys():
            continue
        else:
            # create new key in dict
            entity_dict[topic] = [tags_list[0], num_appear]
    return entity_dict



def entity_filter_search(entities, topics_response):
    entity_dict = dict()
    for entity in entities:
        topic = topics_response.getTopicForm(entity)
        ontology = topics_response.getOntoType(entity)
        num_appear = topics_response.getNumberOfAppearances(entity)
        tags_list = ontology.split(">")

        # remove "Top"
        if len(tags_list) > 1:
            tags_list = tags_list[1:]

        if "Adm1" in tags_list:
            tags_list.append("State")
        # add if already in dict
        if topic in entity_dict.keys():
            for tag in tags_list:
                if tag in entity_dict[topic][0]:
                    continue
                else:
                    entity_dict[topic][0].append(tag)
            entity_dict[topic][1] += num_appear
        else:
            # create new key in dict
            entity_dict[topic] = [tags_list, num_appear]

    return entity_dict

def topics():
    try:
        # We are going to make a request to the Topics Extraction API
        topics_response = meaningcloud.TopicsResponse(meaningcloud.TopicsRequest(license_key, doc=document, lang='en',
                                                                                topicType='e').sendReq())

        # If there are no errors in the request, we print the output
        if topics_response.isSuccessful():
            # print("\nThe request to 'Topics Extraction' finished successfully!\n")

            entities = topics_response.getEntities()
            if entities:
                print("\t Found entities")
                # print("\tEntities detected (" + str(len(entities)) + "):\n")

                # for entity in entities:
                #     print("\t\t" + topics_response.getTopicForm(entity) + ' --> ' +
                #         topics_response.getTypeLastNode(topics_response.getOntoType(entity)) + ' --> ' + 
                #         topics_response.getOntoType(entity) + ' --> ' +
                #         str(topics_response.getNumberOfAppearances(entity)) +"\n")
                    

            else:
                print("\tNo entities detected!\n")
        else:
            if topics_response.getResponse() is None:
                print("\nOh no! The request sent did not return a Json\n")
            else:
                print("\nOh no! There was the following error: " + topics_response.getStatusMsg() + "\n")

        return (topics_response, entities)
    except ValueError:
        e = sys.exc_info()[0]
        print("\nException: " + str(e))

def categorization():
    try:
    # deep categorization api call
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
    except ValueError:
        e = sys.exc_info()[0]
        print("\nException: " + str(e))

def summary():
    try:
    # summary api call
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
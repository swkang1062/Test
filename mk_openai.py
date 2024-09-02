import wrapt
### 중복 wrapping 하면 반복 호출 된다...
###
# OpenAI의 ChatCompletion.create 메소드를 wrapping하는 함수
@wrapt.patch_function_wrapper('openai', 'ChatCompletion.create')
def wrap_chat_completion(wrapped, instance, args, kwargs):
    # 원본 함수 호출
    response = wrapped(*args, **kwargs)

    print("여기서 사용한 Token 수룰 남기면, App. 에서 실수로 남기지 않는 일이 없어진다. ~~~ ")
    print("response['usage'] ==== ", response['usage'])
    print("===================================")

    return response


# LangChain 최신 버젼 (2024/Sep/02)
@wrapt.patch_function_wrapper("langchain_community.chat_models","ChatOpenAI.completion_with_retry")
def log_tokens(wrapped, instance, args, kwargs):
    # 원본 함수 호출
    response = wrapped(*args, **kwargs)
    print("=====================", flush=True)
    print("여기서 사용한 Token 수룰 남기면, App. 에서 실수로 남기지 않는 일이 없어진다. ~~~ ")
    # print("response['usage'] ==== ", response['usage'])
    print("response == ", response.usage)
    usage=response.usage
    print("completion_tokens ==== ", usage.completion_tokens)
    print("prompt_tokens == ", usage.prompt_tokens)
    print("total_tokens == ", usage.total_tokens)

    print("===================================")
    

    return response

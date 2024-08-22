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
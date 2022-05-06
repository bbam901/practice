text = "백제는 3세기 중엽 고이왕 때 ●목지국을 병합하여 한강 유역 대부분을 차지하였으며, 관등제를 정비하고 관리의 복색을 정하는 등 중앙 집권적 지배 체제의토대를 마련하였다. 4세기 중엽에 근초고왕은 마한의 남은 세력을 정복하여 남해안까지 진출하였으며, 고구려를 공격하여 황해도 일대를 차지하였다. 또한, 중국의 동진, 왜와교류하였다."

sentence_list = text.split(".")

sentence = "4세기 중엽에 근초고왕은 마한의 남은 세력을 정복하여 남해안까지 진출하였으며, 고구려를 공격하여 황해도 일대를 차지하였다"

result = [
  ["4세기", "시대"],
  ["중엽에", "기타"],
  ["근초고왕", "인물"],
  ["마한", "지역"],
  ["고이왕", "인물"],
  ["백제", "지역"],
  ["목지국", "지역"],
  ["영조", "인물"],
  ["정조", "인물"],
]

answer = ["근초고왕", "인물"]

# 4세기 중엽에 {}은 마한의 남은 세력을 정복하여 남해안까지 진출하였으며, 고구려를 공격하여 황해도 일대를 차지하였다

# 1. 근초고왕
# 2. 고이왕

result_dict = {}

for value, key in result:
  if key in result_dict:
    result_dict[key].append(value)
  else:
    result_dict[key] = [value]

for key, value in result_dict.items():
  # print(key, value)
  pass

choice_list = []
for item in result_dict[answer[1]]:#-1
  #if item != answer[0]:
    choice_list.append(item)

def get_random_choice(choice_list, count, quesiton_id):
  keys = ["questionId", "choice", "state"]
  result = []

  for i, choice in enumerate(choice_list[:count]):
    result_dict = {}
    for key in keys:
      if key == keys[0]:
        result_dict[key] = quesiton_id
      elif key == keys[1]:
        result_dict[key] = choice
      elif key == keys[2]:
        if(choice=="근초고왕"):
          result_dict[key] = "Answer"
        else:
          result_dict[key] = "WRONG"
    result.append(result_dict)
  return result

print(get_random_choice(choice_list, 4, 1000))


#def generate_blank_question():
  # 질문 생성
 # category = "BLANK"
  #title = "4세기 중엽에 {}은 마한의 남은 세력을 정복하여 남해안까지 진출하였으며, 고구려를 공격하여 황해도 일대를 차지하였다"
  #content = ""
  #comment = "4세기 중엽에 근초고왕은 마한의 남은 세력을 정복하여 남해안까지 진출하였으며, 고구려를 공격하여 황해도 일대를 차지하였다"
  # -> json 응답 만들기
  # response를 받기 -> questionId 90
  # --------------------------------------------------------------------------------

#def generate_choice(questionId, answer, choice_list):
    # 선택지 생성
   # answer = ["근초고왕", "인물"]
    #choice_list = [
      #{'questionId': questionId, 'choice': '근초고왕', 'state': 'ANSWER'},
      #{'questionId': questionId, 'choice': '고이왕', 'state': 'WRONG'}, 
      #{'questionId': questionId, 'choice': '영조', 'state': 'WRONG'}
   # ]
    # request -> 서버에 보내기

#def generate_multiple_question():
  #pass

#def generate_단답_quesiton():
  #pass
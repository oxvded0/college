import json
import os
from ast import literal_eval
from time import sleep

informType = ["journeyName","cityName","roadAddr","groundAddr","latitude","longitude","callNumber","description" ,
"category" ,"url","centerName","cost"]

jsonName = input("지역정보 파일 이름 입력 : ")

with open(f"C:\\traveldata\\{jsonName}.json","r",encoding="utf-8") as f:
      json_data = json.load(f)

cityList = list()
categoryList = list()

jsonType = True
infAmount = 0
informList = dict()
if type(json_data) == dict:
      jsonType = False
      keyValue = input("json파일 여행지 정보 상위 키값을 입력하세요 : ")
      infAmount += len(json_data[keyValue])
      informList = json_data[keyValue]
else:
      infAmount += len(json_data)
      informList = json_data

for i in range(len(informList)):
      overlapChecker = False
      overlapChecker2 = False
      for k in range(len(cityList)):
            if cityList[k] == informList[i]["cityName"]:
                  overlapChecker = True
                  break
      if overlapChecker == False:
            cityList.append(informList[i]["cityName"])
      for k in range(len(categoryList)):
            if categoryList[k] == informList[i]["category"]:
                  overlapChecker2 = True
                  break
      if overlapChecker2 == False:
            categoryList.append(informList[i]["category"])

print(f"현재 {infAmount}개의 여행지 정보가 있습니다.")
sleep(3)

while True:
      os.system('cls')
      print(f"현재 {infAmount}개의 여행지 정보가 있습니다.")
      print("\n\n\n초기메뉴입니다.")
      print("하시려는 작업을 선택해주세요")
      print("1.여행지 정보 추가하기")
      print("2.항목별 여행지 보기/수정/삭제")
      print("3.여행지 검색")
      print("4.json파일 전체보기")
      print("5.프로그램을 종료")
      userChoice = int(input("숫자 입력 : "))

      if userChoice == 1:
            os.system('cls')
            print(f"현재 {infAmount}개의 여행지 정보가 있습니다.")
            print("초기메뉴로 돌아가시려면 0번 여행지 정보를 추가하시려면 그 외 숫자를 입력해주세요")
            addedInform = dict()
            duplicateChecker = False
            duplicateSites = list()
            duChoice = 1

            resetFirst = int(input("숫자입력 : "))
            if resetFirst == 0:
                  continue

            siteName = input("여행지 이름 : ")


            snCharacterList = list()

            for i in range(len(siteName)):
                  snCharacterList.append(siteName[i])

            for i in range(len(informList)):
                  journeyName = informList[i]["journeyName"]
                  jnCharacterList = list()
                  count = 0
                  for k in range(len(journeyName)):
                        jnCharacterList.append(journeyName[k])

                  for k in range(len(jnCharacterList)):
                        for j in range(len(snCharacterList)):
                              if jnCharacterList[k] == snCharacterList[j]:
                                    count+=1
                                    break

                  if len(journeyName) - count <=2:
                        duplicateChecker = True
                        duplicateSites.append(journeyName)
            
            if duplicateChecker == True:
                  print("비슷한 이름의 여행지가 이미 존재합니다. 중복된 것인지 확인해주세요.")
                  print(f"중복된 여행지 리스트 {duplicateSites}")
                  print("2.여행지 추가 초기화면으로 되돌아가려면 2번")
                  print("계속 추가하시려면 그 외 아무 숫자나 입력해주세요")
                  duChoice = int(input("입력 : "))
            else:
                  print("중복되는 여행지가 없습니다.")
            if duChoice == 2:
                  continue
            
            print("추가할 여행지의 정보를 입력해주세요")
            for i in range(len(informType)):
                  siteInform = input(f"{informType[i]} : ")
                  addedInform[informType[i]] = siteInform
            os.system("cls")
            print("추가할 여행지")
            for z,x in addedInform.items():
                  print(f"{z} : {x}")

            checkQ = input("추가하시겠습니까? y/n : ")

            if checkQ == "y":            
                  if jsonType == False:
                        json_data[keyValue].append(addedInform)
                        print("여행지가 추가되었습니다.")
                        sleep(3)
                  
                  else:
                        json_data.append(addedInform)
                        print("여행지가 추가되었습니다.")
                        sleep(3)
            else:
                  print("취소되었습니다")
                  print("초기화면으로 되돌아갑니다.")
                  sleep(3)
      
      elif userChoice == 2:
            os.system('cls')
            print(f"현재 {infAmount}개의 여행지 정보가 있습니다.")
            print("항목을 선택해주세요")
            print("1.시군구별")
            print("2.카테고리별")
            print("그 외 숫자를 입력하시면 초기화면으로 돌아갑니다.")
            selectDetail = int(input("숫자 입력 : "))

            arrayNumberCT = 0

            selectedCitySite = list()
            selectedSiteName = list()
            
            if selectDetail == 1:
                  print("시군구 목록입니다")
                  for i in range(len(cityList)):
                        print(f"{i+1}. {cityList[i]}")
                  cityChoice=int(input("도시의 번호 입력 : "))
                  forCity = cityList[cityChoice-1]

                  tempNumber = 0

                  for i in range(len(informList)):
                        if forCity == informList[i]["cityName"]:
                              selectedSiteName.append(informList[i]["journeyName"])
                  print(f"{forCity} 여행지 목록입니다.")
                  for i in range(len(selectedSiteName)):
                        print(f"{i+1}. {selectedSiteName[i]}")

                  print("자세히 보길 원하시면 여행지 번호, 초기메뉴로 돌아가려면 0번을 눌러주세요")
                  siteChoice=int(input("숫자 입력 : "))
                  if siteChoice == 0:
                        continue
                  finalChoice = selectedSiteName[siteChoice-1]

                  if jsonType == False:

                        listDetails = list()
                        for i in range(len(json_data[keyValue])):
                              if finalChoice == json_data[keyValue][i]["journeyName"]:
                                    arrayNumberCT += i
                        print("여행지 세부정보")
                        for k, v in json_data[keyValue][arrayNumberCT].items():
    
                              print("{!r:15s} : {}".format(k, v))
                        
                        print("수정을 원하시면 1번")
                        print("삭제를 원하시면 2번")
                        print("초기화면으로 되돌아 가시려면 3번을 입력해주세요")
                        secondFinal = int(input("숫자 입력 : "))

                        if secondFinal == 3:
                              continue

                        if secondFinal == 2:
                              json_data[keyValue].remove(json_data[keyValue][arrayNumberCT])
                              sleep(3)
                              os.system('cls')
                              print("삭제가 완료되었습니다.")
                              sleep(3)
                        if secondFinal == 1:
                              for i in json_data[keyValue][arrayNumberCT].keys():
                                    listDetails.append(i)
                              for i in range(len(listDetails)):
                                    print(f"{i+1}. {listDetails[i]}")
                              print("수정을 원하시는 항목의 숫자를 입력해주세요. 0번 입력시 초기화면")

                              modifyingChoice = int(input("숫자 입력 : "))
                              if modifyingChoice == 0:
                                    continue
                              modifyingChoice-=1
                              print(f"수정 전 항목 : {listDetails[modifyingChoice]} : {json_data[keyValue][arrayNumberCT][listDetails[modifyingChoice]]}")
                              modifyingInput = input("수정 할 항목을 입력해주세요 : ")
                              print(f"수정 전 항목 : {listDetails[modifyingChoice]} : {json_data[keyValue][arrayNumberCT][listDetails[modifyingChoice]]}")
                              print(f"수정 후 항목 : {listDetails[modifyingChoice]} : {modifyingInput}")

                              veriffying = input("수정 하시겠습니까? y/n : ")

                              if veriffying == "y":
                                    json_data[keyValue][arrayNumberCT][listDetails[modifyingChoice]] = modifyingInput
                                    sleep(3)
                                    os.system('cls')
                                    print("수정되었습니다.")
                                    sleep(3)
                              else:
                                    sleep(3)
                                    os.system('cls')
                                    print("취소되었습니다.")
                                    print("초기화면으로 되돌아갑니다.")
                                    sleep(3)
                        
                  else:
                        print("여행지 세부정보")
                        print(json_data[arrayNumberCT])
                        for i in json_data[arrayNumberCT].keys():
                              print(i, end= " ")
                        listDetails = list()
                        for i in range(len(json_data)):
                              if finalChoice == json_data[i]["journeyName"]:
                                    arrayNumberCT += i
                        print("여행지 세부정보")
                        for k, v in json_data[arrayNumberCT].items():
        
                              print("{!r:15s} : {}".format(k, v))
                        
                        print("수정을 원하시면 1번")
                        print("삭제를 원하시면 2번")
                        print("초기화면으로 되돌아 가시려면 3번을 입력해주세요")
                        secondFinal = int(input("숫자 입력 : "))

                        if secondFinal == 3:
                              continue

                        if secondFinal == 2:
                              json_data.remove(json_data[arrayNumberCT])
                              sleep(3)
                              os.system('cls')
                              print("삭제가 완료되었습니다.")
                              sleep(3)
                        if secondFinal == 1:
                              for i in json_data[arrayNumberCT].keys():
                                    listDetails.append(i)
                              for i in range(len(listDetails)):
                                    print(f"{i+1}. {listDetails[i]}")
                              print("수정을 원하시는 항목의 숫자를 입력해주세요. 0번 입력시 초기화면")

                              modifyingChoice = int(input("숫자 입력 : "))
                              if modifyingChoice == 0:
                                    continue
                              modifyingChoice-=1
                              print(f"수정 전 항목 : {listDetails[modifyingChoice]} : {json_data[arrayNumberCT][listDetails[modifyingChoice]]}")
                              modifyingInput = input("수정 할 항목을 입력해주세요 : ")
                              print(f"수정 전 항목 : {listDetails[modifyingChoice]} : {json_data[arrayNumberCT][listDetails[modifyingChoice]]}")
                              print(f"수정 후 항목 : {listDetails[modifyingChoice]} : {modifyingInput}")

                              veriffying = input("수정 하시겠습니까? y/n : ")

                              if veriffying == "y":
                                    json_data[arrayNumberCT][listDetails[modifyingChoice]] = modifyingInput
                                    sleep(3)
                                    os.system('cls')
                                    print("수정되었습니다.")
                                    sleep(3)
                              else:
                                    sleep(3)
                                    os.system('cls')
                                    print("취소되었습니다.")
                                    print("초기화면으로 되돌아갑니다.")
                                    sleep(3)
                  
            elif selectDetail == 2:
                  print("카테고리 목록입니다")
                  for i in range(len(categoryList)):
                        print(f"{i+1}. {categoryList[i]}")
                  categoryChoice=int(input("도시의 번호 입력 : "))
                  forcategory = categoryList[categoryChoice-1]

                  tempNumber = 0

                  for i in range(len(informList)):
                        if forcategory == informList[i]["category"]:
                              selectedSiteName.append(informList[i]["journeyName"])
                  print(f"{forcategory} 여행지 목록입니다.")
                  for i in range(len(selectedSiteName)):
                        print(f"{i+1}. {selectedSiteName[i]}")

                  print("자세히 보길 원하시면 여행지 번호, 초기메뉴로 돌아가려면 0번을 눌러주세요")
                  siteChoice=int(input("숫자 입력 : "))
                  if siteChoice == 0:
                        continue
                  finalChoice = selectedSiteName[siteChoice-1]

                  if jsonType == False:
    
                        listDetails = list()
                        for i in range(len(json_data[keyValue])):
                              if finalChoice == json_data[keyValue][i]["journeyName"]:
                                    arrayNumberCT += i
                        print("여행지 세부정보")
                        for k, v in json_data[keyValue][arrayNumberCT].items():
    
                              print("{!r:15s} : {}".format(k, v))
                        print("수정을 원하시면 1번")
                        print("삭제를 원하시면 2번")
                        print("초기화면으로 되돌아 가시려면 3번을 입력해주세요")
                        secondFinal = int(input("숫자 입력 : "))

                        if secondFinal == 3:
                              continue

                        if secondFinal == 2:
                              json_data[keyValue].remove(json_data[keyValue][arrayNumberCT])
                              sleep(3)
                              os.system('cls')
                              print("삭제가 완료되었습니다.")
                              sleep(3)
                        if secondFinal == 1:
                              for i in json_data[keyValue][arrayNumberCT].keys():
                                    listDetails.append(i)
                              for i in range(len(listDetails)):
                                    print(f"{i+1}. {listDetails[i]}")
                              print("수정을 원하시는 항목의 숫자를 입력해주세요. 0번 입력시 초기화면")

                              modifyingChoice = int(input("숫자 입력 : "))
                              if modifyingChoice == 0:
                                    continue
                              modifyingChoice-=1
                              print(f"수정 전 항목 : {listDetails[modifyingChoice]} : {json_data[keyValue][arrayNumberCT][listDetails[modifyingChoice]]}")
                              modifyingInput = input("수정 할 항목을 입력해주세요 : ")
                              print(f"수정 전 항목 : {listDetails[modifyingChoice]} : {json_data[keyValue][arrayNumberCT][listDetails[modifyingChoice]]}")
                              print(f"수정 후 항목 : {listDetails[modifyingChoice]} : {modifyingInput}")

                              veriffying = input("수정 하시겠습니까? y/n : ")

                        if veriffying == "y":
                              json_data[keyValue][arrayNumberCT][listDetails[modifyingChoice]] = modifyingInput
                              sleep(3)
                              os.system('cls')
                              print("수정되었습니다.")
                              sleep(3)
                        else:
                              sleep(3)
                              os.system('cls')
                              print("취소되었습니다.")
                              print("초기화면으로 되돌아갑니다.")
                              sleep(3)
                        
                  else:
                        print("여행지 세부정보")
                        print(json_data[arrayNumberCT])
                        for i in json_data[arrayNumberCT].keys():
                              print(i, end= " ")
                        listDetails = list()
                        for i in range(len(json_data)):
                              if finalChoice == json_data[i]["journeyName"]:
                                    arrayNumberCT += i
                        print("여행지 세부정보")
                        for k, v in json_data[arrayNumberCT].items():
        
                              print("{!r:15s} : {}".format(k, v))
                        print("수정을 원하시면 1번")
                        print("삭제를 원하시면 2번")
                        print("초기화면으로 되돌아 가시려면 3번을 입력해주세요")
                        secondFinal = int(input("숫자 입력 : "))

                        if secondFinal == 3:
                              continue

                        if secondFinal == 2:
                              json_data.remove(json_data[arrayNumberCT])
                              sleep(3)
                              os.system('cls')
                              print("삭제가 완료되었습니다.")
                              sleep(3)
                        if secondFinal == 1:
                              for i in json_data[arrayNumberCT].keys():
                                    listDetails.append(i)
                              for i in range(len(listDetails)):
                                    print(f"{i+1}. {listDetails[i]}")
                              print("수정을 원하시는 항목의 숫자를 입력해주세요. 0번 입력시 초기화면")

                              modifyingChoice = int(input("숫자 입력 : "))
                              if modifyingChoice == 0:
                                    continue
                              modifyingChoice-=1
                              print(f"수정 전 항목 : {listDetails[modifyingChoice]} : {json_data[arrayNumberCT][listDetails[modifyingChoice]]}")
                              modifyingInput = input("수정 할 항목을 입력해주세요 : ")
                              print(f"수정 전 항목 : {listDetails[modifyingChoice]} : {json_data[arrayNumberCT][listDetails[modifyingChoice]]}")
                              print(f"수정 후 항목 : {listDetails[modifyingChoice]} : {modifyingInput}")

                              veriffying = input("수정 하시겠습니까? y/n : ")

                              if veriffying == "y":
                                    json_data[arrayNumberCT][listDetails[modifyingChoice]] = modifyingInput
                                    sleep(3)
                                    os.system('cls')
                                    print("수정되었습니다.")
                                    sleep(3)
                              else:
                                    sleep(3)
                                    os.system('cls')
                                    print("취소되었습니다.")
                                    print("초기화면으로 되돌아갑니다.")
                                    sleep(3)
         
            else:
                  continue

      elif userChoice == 3:
            os.system('cls')
            print(f"현재 {infAmount}개의 여행지 정보가 있습니다.")
            print("검색할 여행지를 입력해주세요. 0번 입력시 초기화면")
            userSeaching = input("여행지 입력 : ")
            if userSeaching == "0":
                  continue
            usCharacterList = list()
            duplicateSites = list()
            arraySequence = list()

            for i in range(len(userSeaching)):
                  usCharacterList.append(userSeaching[i])

            for i in range(len(informList)):
                  journeyName = informList[i]["journeyName"]
                  jnCharacterList = list()
                  count = 0
                  for k in range(len(journeyName)):
                        jnCharacterList.append(journeyName[k])

                  for k in range(len(jnCharacterList)):
                        for j in range(len(usCharacterList)):
                              if jnCharacterList[k] == usCharacterList[j]:
                                    count+=1
                                    break
                  if len(journeyName) - count <=2:
                        duplicateChecker = True
                        duplicateSites.append(journeyName)
                        arraySequence.append(i)
            print("검색결과")
            for i in range(len(duplicateSites)):
                  print(f"{i+1}. {duplicateSites[i]}")
            print("자세한 내용을 보려면 여행지의 번호를 입력 \n 초기화면으로 돌아가시려면 0번을 눌러주세요")
            userThird = int(input("숫자 입력 : "))
            if userThird == 0:
                  continue

            for k, v in informList[arraySequence[userThird-1]].items():
        
                              print("{!r:15s} : {}".format(k, v))

            initialMenu=(input("엔터키를 누르시면 초기화면으로 돌아갑니다"))
            if initialMenu != "adfkfhnjajkfhadfjk":
                  continue
           
      elif userChoice == 4:
            print(json.dumps(json_data, ensure_ascii=False, indent="\t") )
            initialF=(input("초기화면으로 돌아가시려면 엔터키를 눌러주세요"))
            if initialF != "dsafkjkajiencvzml":
                  continue

      elif userChoice == 5:
            os.system('cls')
            sleep(3)
            print(f"현재 {infAmount}개의 여행지 정보가 있습니다.")
            print("프로그램을 종료합니다")
            sleep(3)
            with open(f"C:\\traveldata\\{jsonName}.json", 'w',decoding="utf-8") as outfile:
                  json.dump(json_data, outfile, indent=4)
            break
      
      else:
            print("1에서 5 사이의 숫자만을 입력해주세요")


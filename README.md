# Introduce
The written article is automatically uploaded to the Tistory blog.




<br><br>

##  TODO
---
- 새로운 md 파일이 생성된 후 main에 push를 하면 github actions이 실행된다. 
- github actions에서 새로 생성된 md 파일을 파일이름으로 구분하여 가져온 후 title을 전역변수로 만든다. 
- md 파일을 지정된 장소에 target.md로 복사하고 tistory_auto_uploader.main.py를 실행한다. 
- run 함수를 통해 target.md을 html 형식으로 바꾸어 post_write 함수로 보낸다.
- (추가)성공여부와 새로 작성된 포스팅 링크를 카카오톡으로 보내준다.

<br><br>

## Reference
---
Api docs - https://tistory.github.io/document-tistory-apis/

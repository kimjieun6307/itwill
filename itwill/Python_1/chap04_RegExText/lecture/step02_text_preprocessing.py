# 텍스트 전처리
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
print(len(texts), type(texts)) #3 <class 'list'>

from re import sub # R의 gsub() 유사함
# from pachage.module import class or function
# from module import class or function ---> re : module, sub : function

# 불용어 제거 : 특수문자, 숫자, 문자부호 제거
# 1. 소문자 변경 : .lower()
print('소문자 변경')
for text in texts :
    print(text.lower())
'''
소문자 변경
afab54747,asabag?
abtta $$;a12:2424.
uysfsfa,a124&***$? '''
texts_re=[text.lower() for text in texts ]
print('texts_re1 : ', texts_re) # texts_re1 :  ['afab54747,asabag?', 'abtta $$;a12:2424.', 'uysfsfa,a124&***$?']

# 2. 숫자 제거 : sub('[0-9]','',text)
texts_re2 = [ sub('[0-9]','',text) for text in texts_re]
print('texts_re2 : ', texts_re2) # texts_re2 :  ['afab,asabag?', 'abtta $$;a:.', 'uysfsfa,a&***$?']

# 3. 문장부호 제거
punc_str = '[.,;:?!]'
text_re3 = [sub(punc_str, '', text) for text in texts_re2]
print('texts_re3 : ', text_re3) # texts_re3 :  ['afabasabag', 'abtta $$a', 'uysfsfaa&***$']

# 4. 특수문자 제거
spec_str = '[@#$%^&*()]'
text_re4= [sub(spec_str, '', text) for text in text_re3]
print('texts_re4 : ', text_re4) # texts_re4 :  ['afabasabag', 'abtta a', 'uysfsfaa']

# 5. 공백 제거 : split('abtta a'-> 'abtta', 'a'), ''.join('abtta', 'a') =>'abttaa'
text_re5 = [ ''.join(text.split()) for text in text_re4]
print('text_re5 : ', text_re5) # text_re5 :  ['afabasabag', 'abttaa', 'uysfsfaa']










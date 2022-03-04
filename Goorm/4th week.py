num=1 #포매팅에 사용할 유일한 변수
law = """대한민국 헌법
제1장 총강
제1조
\t{0}. 대한민국은 민주공화국이다.
\t{1}. 대한민국의 주권은 \'국민\'에게 있고, 모든 권력은 \'국민\'으로부터 나온다.
제2조
\t1. 대한민국의 \'국민\'이 되는 요건은 법률로 정한다.
\t{1}. 국가는 법률이 정하는 바에 의하여 재외\'국민\'을 보호할 의무를 진다.
제3조
\t{0}. 대한민국의 영토는 한반도와 그 부속도서로 한다.""" .format(num,2)

print(law)
print(law.count("법률"))
print(law.find("주권"))
print(law.replace("대한민국","한국"))
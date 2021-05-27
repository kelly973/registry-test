from confluent_kafka.schema_registry import SchemaRegistryClient # confluent-kafka 라이브러리 활용
conf = {'url':'http://0.0.0.0:8085'}  # schema registry 호스트 지정
client = SchemaRegistryClient(conf) # schema registry client 생성

from confluent_kafka.schema_registry import Schema

f = open('../sample.proto','r')
new_str = f.read().__str__()
    
new_schema = Schema(new_str, 'PROTOBUF',references=[]) # 신규 스키마 생성
res = client.register_schema('new_schema_test',new_schema) # 신규 스키마 레지스트리에 등록

print(res)

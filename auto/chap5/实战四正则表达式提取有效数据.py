# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import re

s='{"bankCode":"CCB","corpIdCodeCore":"916500007318073269","corpIdCodeFinance":"91510100MA6DDWNN21","corpIdCodeSource":"91510100MA69MUBX8Q","corpIdTypeCore":"BUSINESS_LICENSE_SZ","corpIdTypeFinance":"BUSINESS_LICENSE_SZ","corpIdTypeSource":"BUSINESS_LICENSE_SZ","corpNameCore":"中建西部建设股份有限公司","corpNameFinance":"中建蓉成建材成都有限公司煎茶分公司","corpNameSource":"砼联数字科技有限公司","creditAmountFinance":300000.00,"creditCount":2,"credits":[{"corpIdCodeThis":"916500007318073269","corpIdTypeThis":"BUSINESS_LICENSE_SZ","corpNameThis":"中建西部建设股份有限公司","creditAmountThis":300000.00,"creditSerial":1,"pkCorpThis":"TN2022042700010413","pkCreditParent":"-1","pkCreditThis":"BT2022070115181354400010601","transferDate":"2022-07-01"},{"corpIdCodeThis":"91510100MA6DDWNN21","corpIdTypeThis":"BUSINESS_LICENSE_SZ","corpNameThis":"中建蓉成建材成都有限公司煎茶分公司","creditAmountThis":300000.00,"creditSerial":2,"pkCorpThis":"TN2022022600001213","pkCreditParent":"BT2022070115181354400010601","pkCreditThis":"BT2022070409243706400010801","transferDate":"2022-07-01"}],"financeDoc":{"businessLicenseFileId":"3b75a04a-7d42-42b6-b0ae-ff970bfa57eb","caAuthFileId":"8ff84bb2-1468-4f2b-8478-9673457d139e","legalIdCardFileId":"202dbaa1-928e-44c1-bb9d-a378324c6fde"},"invoice":{"addressDetail":"发士大夫111","addressPhone":"17755475511","bankAccount":"465456444111","bankName":"史蒂夫111","contactAddress":"士大夫","contactCity":"丹东市","contactCounty":"元宝区","contactFixedPhone":"028-85476511","contactMobilePhone":"14547565511","contactName":"收件人11","contactProvince":"辽宁省","corpName":"中建蓉成建材成都有限公司煎茶分公司","department":"发到付11","emailAddress":"5116511@qq.com","taxId":"131231231233234"},"legalPerson":{"idCode":"362531198704175434","idType":"RESIDENT_IDC","personName":"王兵和"},"loanFileInfo":[{"fileId":"742bd96f-da73-45b3-b45e-0938e324b653","fileType":"PARTNER_COMMITMENT_LETTER"}],"maturityAmount":300000.00,"maturityDate":"2022-10-19","operator":{"idCode":"513224455365475651","idType":"RESIDENT_IDC","mobilePhone":"17745475585","personName":"张三1"},"pkCorpCore":"TN2022042700010413","pkCorpFinance":"TN2022022600001213","pkCreditFinance":"BT2022070409243706400010801"}'

pattern=r'\W[A-Z0-9]{18}\W'

print(re.findall(pattern,s))

pattern2=r'BT[0-9]+'
print(re.findall(pattern2,s))

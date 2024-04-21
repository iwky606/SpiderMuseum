import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models

if __name__ == "__main__":
    try:
        cred = credential.Credential("", "")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

        req = models.TextTranslateBatchRequest()
        params = {
            "Source": "de",
            "Target": "zh",
            "ProjectId": 0,
            "SourceTextList": [
                '''              ''',
            ]
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextTranslateBatch(req)

        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)
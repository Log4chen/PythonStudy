from httprunner import HttpRunner, Config, Step, RunRequest


class TestMarket(HttpRunner):
    config = (
        Config("供应商服务市场配置")
        .verify(False)
        .base_url("${ENV(service-baseurl)}")
        .variables(**{
            "market": "全国",
            "employeenumber": "${ENV(pm_user)}"
        })
    )

    teststeps = [
        Step(
            RunRequest("查询供应商")
            .get("supplier/querySupplierInfo")
            .with_headers(**{
                "Client": "MCDBoss",
                "employeenumber": "$employeenumber"
            })
            .with_params(**{"keyWord": "南京苏宁软件技术有限公司"})
            .validate()
            .assert_equal("body.data[0].supplierId", "46934")
        ),
        Step(
            RunRequest("新增供应商市场配置")
            .post("/marketConfig/add")
            .with_headers(**{
                "Client": "MCDBoss",
                "employeenumber": "$employeenumber"
            })
            .with_json({"supplierId":"11003","supplierType":"1","scope":2,"market":"北京","supplierName":"朱英"})
            .validate()
            .assert_equal("body.code", 200)
            .assert_equal("${sleep_seconds(5)}", True, "等待5秒")
        ),
        Step(
            RunRequest("查询列表")
            .post("/marketConfig/queryPageList")
            .with_headers(**{
                "Client": "MCDBoss",
                "employeenumber": "$employeenumber"
            })
            .with_json({"supplierId":"41166","pageNo":1,"pageSize":20})
            .validate()
            .assert_equal("body.data.list[0].supplierName", "深圳市法本信息技术股份有限公司")

        )
    ]

if __name__ == "__main__":
    TestMarket().test_start()
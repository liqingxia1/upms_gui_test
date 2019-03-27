## 2018/10/31
## liqingx

#1.代码结构
- 执行 run_all.py 可运行所有用例
        
        
        -ConfigParser                   	配置文件目录
        ————config.ini                  		配置文件
        -screenshot                     	测试时保存的截图目录
		
        -src                            	《代码目录》
        ————general                     		《通用的操作封装目录》
        ————————browser_operation.py    		对浏览器的通用操作封装
        ————user_manage                 		《用户管理目录》
        ————————user_details.py         		用户详情界面的操作
        ————config.py                   		配置文件的读取
        ————login.py                    		登录操作
        ————open_bw.py                  		打开浏览器
		
        -ts_case                        	《测试用例目录》
        ————case                        		《用例集合的目录》
        ————————test_login.py           		登录的测试用例
        ————————test_user_details.py    		用户详情界面的用例
		
        ————report                      	《生成测试报告的目录》
        ————————report.html             		测试报告
		
        ————run_all.py                  	运行可执行所有用例








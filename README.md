这是DATA620004期末作业的工程仓库，其中:
	1.TensoRF为任务1工程;
 
	2.gaussian-splatting为任务2工程;
 
	3.script为获取样本、转换格式与渲染视频的脚本;
 
	4.数据及生成的模型权重可通过以下链接下载：
	链接: https://pan.baidu.com/s/1ZgBX0AvwsvH-7SZLlTDniA?pwd=jjir 提取码: jjir

运行方式：

	TensoRF
	1.进入TensoRF目录，将网盘data\0621_2放到data文件夹中
	2.通过 Python train.py –-config config/yang_f.py 开启训练，可通过配置文件指定具体参数
	3.可通过 Python train.py –-config config/yang_f.py –-ckpt log/tensoRF/tensoRF.th –render_only 1 –render_path 1 用新路径渲染视频，具体路径可通过dataLoader/llff.py中的render_path_spiral指定。
	4.生成结果在log文件夹中，已上传至网盘\model\tensoRF
	
	gaussian-splatting
	1.进入gaussian-splatting目录，将网盘\data\gaussian放之data文件夹中
	2.通过Python train.py -s data/ gaussian 开启训练，可参照gaussian-splatting中README教程或修改arguments/__init__.py指定具体参数
	3.通过python render_custom.py -m output/b3cbc0df-0/ 用新路径渲染，请将地址参数替换为生成结果，具体路径可通过render_custom.py中generate_views_example函数与generate_circle_views函数指定
	4.生成结果在output文件夹中，已上传至网盘model\3D_gaussian，项目只生成视频帧，可使用script/video.py脚本将cusotm/ours_30000/renders中的图片转换为视频，网盘中model\3D_gaussian\render.mp4为已转换的自定义路径的视频，model\3D_gaussian\render2.mp4为按训练路径渲染的视频。

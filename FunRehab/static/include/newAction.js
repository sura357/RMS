// JavaScript Document

// 宣告---
var patientID = "";  // 選擇病患
	
var action = 
	{
		name: "",     // 動作名稱
		duration: 0,  // 次數
		bread: 0,     // 休息時間
		ontop: 0,     // 頂點維持時間
		type: 0,      // 動作類型
		motion: 0,    // 動作花費時間
	};
var saveAction = [];  // 存檔action(array)  // 放置 action
var presetAction = ["動作1", "動作2", "動作3"];  // 動作有哪些

var planName = document.getElementById("planName");  // 計畫名稱
var patient = document.getElementById("patient");  // 病患
var actionGather = document.getElementById("actionGather");  // 動作集合
var addBtn = document.getElementById("addBtn");  // 新增按鈕
var saveBtn = document.getElementById("saveBtn");  // 存檔按鈕
var patientBtn = document.getElementById("patientBtn");  // 選擇病患按鈕


// 函式---
function clear_action()  // 清空動作
{
	actionGather.innerHTML = "";
}

function stringToHTML(str)  // 字串轉html
{ 
	var dom = document.createElement('div'); 
	dom.innerHTML = str; 
	return dom;
}

function add_action(html)  // 加入動作html
{
	var node = stringToHTML(html);
	actionGather.appendChild(node);
}

function return_action(selectName)  // 回傳動作字串 // 動作名稱(array)
{
	var actionHtml = "<li class='reto-div horizaCenter'>\
					<div class='reto-poject-p'>\
						<p>動作名稱</p>\
						<p>動作次數</p>\
						<p>休息時間</p>\
						<p>頂點維持時間</p>\
						<p>動作類型</p>\
						<p>動作花費時間</p>\
					</div>\
					<div class='reto-poject-in'>\
						<p class='reto-poject-p-div'>\
							<select class='reto-div-input reto-div-select'>";

	for(var i=0;i<selectName.length;i++)
	{
		actionHtml = actionHtml + "<option>" + selectName[i] + "</option>";
	}


	actionHtml = actionHtml + "</select>\
						</p>\
						<p class='reto-poject-p-div'><input class='reto-div-input' type='text'/></p>\
						<p class='reto-poject-p-div'><input class='reto-div-input' type='text'/></p>\
						<p class='reto-poject-p-div'><input class='reto-div-input' type='text'/></p>\
						<p class='reto-poject-p-div'><input class='reto-div-input' type='text'/></p>\
						<p class='reto-poject-p-div'><input class='reto-div-input' type='text'/></p>\
					</div>\
				</li>";

	return actionHtml;
}

// 事件---
patientBtn.addEventListener('click',function(event){  // 選擇病患
	patientID = patient.value;
	console.log("選擇病患: ", PatientID);
},false);

addBtn.addEventListener('click',function(event){  // 新增
	var actionHtml = return_action(presetAction);
	add_action(actionHtml);
	console.log("新增空動作");
},false);

saveBtn.addEventListener('click',function(event){  // 存檔

	console.log("存檔");
},false);







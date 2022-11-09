// JavaScript Document

// 宣告---
var yearLeftBtn = document.getElementById("yearLeftBtn");
var yearRightBtn = document.getElementById("yearRightBtn");
var monLeftBtn = document.getElementById("monLeftBtn");
var monRightBtn = document.getElementById("monRightBtn");
var yearDiv = document.getElementById("yearDiv");
var monthDiv = document.getElementById("monthDiv");

// 函式---
function monthlyBtn(event) // 選擇日期
{  
	var dateP = document.getElementById("dateP");
	var date = event.split("-");
	var mon;
	var day;
	var choosedate;

	choosedate = date[0] + date[1] + date[2]
	selectingDate.year = date[0];
	selectingDate.month = date[1];
	selectingDate.day = date[2];
	
	mon = parseInt(date[1]).toString();
	day = parseInt(date[2]).toString();


	if(selectedDate.includes(choosedate)){
		delete selectedDate[selectedDate.indexOf(choosedate)];
		delete Action_amount[choosedate];
		delete set_detail[selectedDate.indexOf(choosedate)];
		selectedDate = selectedDate.filter(function () { return true });
		//Action_amount = selectedDate.filter(function () { return true });
		//set_detail = selectedDate.filter(function () { return true });

		$("#sel_dates option[value='"+choosedate+"']").remove();
	}
	else {
		selectedDate.push(choosedate);
		Action_amount[choosedate]=0;
		$('#sel_dates').append($('<option>', {
			value: choosedate,
			text : choosedate
		}));
	}

	$.each(selectedDate, function (i, date) {

	});
	console.log(selectedDate);  // 20220925
	
	if (dateP != null)
		dateP.innerHTML = mon + "月" + day + "日";
	upMonthlyData(presetDate, selectingDate, selectedDate, model);
}

function setYear(difference)  // 調整年分
{
	var today = new Date();
	var curYear = today.getFullYear();
	var Year = presetDate.year + difference;

	if (Year < curYear - 10)
	{
		console.log("年份只到", curYear - 10);
		return true;
	}
	else if (Year > curYear + 10)
	{
		console.log("年份只到", curYear + 10);
		return true;
	}

	presetDate.year = Year;
	yearDiv.innerHTML = presetDate.year + "年";
	upMonthlyData(presetDate, selectingDate, selectedDate, model);
	return false;
}

function setMonth(difference)  // 調整月分
{
	var month = presetDate.month + difference;
	if (month < 1)
	{
		month = 12;
		
		if(setYear(-1))
			return;
	}
	else if (month > 12)
	{
		month = 1;
		if(setYear(1))
			return;
	}
	
	presetDate.month = month;
	monthDiv.innerHTML = presetDate.month + "月";
	upMonthlyData(presetDate, selectingDate, selectedDate, model);
}

// 事件----
yearLeftBtn.addEventListener('click',function(event){
	setYear(-1);
},false);

yearRightBtn.addEventListener('click',function(event){
	setYear(1);
},false);

monLeftBtn.addEventListener('click',function(event){
	setMonth(-1);
},false);

monRightBtn.addEventListener('click',function(event){
	setMonth(1);
},false);



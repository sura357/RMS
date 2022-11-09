// JavaScript Document

function project_print(name, action, time, exact, great)  // 復健計畫名稱, 動作名稱, 時間, 準確率, 好棒
{
	var ContentStart = "<div class='monthly-project-content'>";
	var ContentEnd = "</div>";
	var leftStart = "<div class='monthly-project-left'>";
	var leftEnd = "</div>";
	var rightStart = "<div class='monthly-project-right'>";
	var rightEnd = "</div>";
	var pStart = "<p>";
	var pEnd = "</p>";
	var img = "<img class='monthly-project-img' src='pic/great.png' alt='' width='60px' height='60px'/>";

	var projectHtml = "";
	projectHtml += ContentStart;
	projectHtml += leftStart;
	projectHtml += pStart;
	projectHtml += name;
	projectHtml += pEnd;
	projectHtml += pStart;
	projectHtml += "項目: " + action;
	projectHtml += pEnd;
	projectHtml += pStart;
	projectHtml += "時間: " + time;
	projectHtml += pEnd;
	projectHtml += pStart;
	projectHtml += "準確率: " + exact;
	projectHtml += pEnd;
	projectHtml += leftEnd;
	projectHtml += rightStart;

	if (great)
		projectHtml += img;

	projectHtml += rightEnd;
	projectHtml += ContentEnd;

	document.write(projectHtml);
}
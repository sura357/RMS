// JavaScript Document
function monthly_print(model)  // 打印 月曆  // 模式 (true->一般使用者, false->復健師)
{
	var datetime = new Date();
	var tableHtml = "<table class='monthly" + ((model == false) ? (" reto-monthly") : ("")) + "'>\
	<thead>\
		<tr>\
			<th colspan='7'>\
				<div class='monthly-row'>\
					<div class='monthly-row'>\
						<button class='btn' id='yearLeftBtn'><img src='/static/pic/left.png' alt='' width='15px' height='15px'></button>\
						<div id='yearDiv' class='monthly-year'>"+(datetime.getFullYear())+"年</div>\
						<button class='btn' id='yearRightBtn'><img src='/static/pic/right.png' alt='' width='15px' height='15px'></button>\
					</div>\
					<div class='monthly-row'>\
						<button class='btn' id='monLeftBtn'><img src='/static/pic/left.png' alt='' width='15px' height='15px'></button>\
						<div id='monthDiv' class='monthly-month'>"+(datetime.getMonth()+1)+"月</div>\
						<button class='btn' id='monRightBtn'><img src='/static/pic/right.png' alt='' width='15px' height='15px'></button>\
					</div>\
				</div>\
			</th>\
		</tr>\
		<tr class='monthly-div-tr'>\
			<th><div class='monthly-div-th" + ((model == false) ? (" reto-th") : ("")) + "'><center>一</center></div></th>\
			<th><div class='monthly-div-th" + ((model == false) ? (" reto-th") : ("")) + "'><center>二</center></div></th>\
			<th><div class='monthly-div-th" + ((model == false) ? (" reto-th") : ("")) + "'><center>三</center></div></th>\
			<th><div class='monthly-div-th" + ((model == false) ? (" reto-th") : ("")) + "'><center>四</center></div></th>\
			<th><div class='monthly-div-th" + ((model == false) ? (" reto-th") : ("")) + "'><center>五</center></div></th>\
			<th><div class='monthly-div-th" + ((model == false) ? (" reto-th") : ("")) + "'><center>六</center></div></th>\
			<th><div class='monthly-div-th" + ((model == false) ? (" reto-th") : ("")) + "'><center>日</center></div></th>\
		</tr>\
	</thead>\
	<tbody id='tbody'>\
		<tr>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
		</tr>\
		<tr>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
		</tr>\
		<tr>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
		</tr>\
		<tr>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
		</tr>\
		<tr>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
		</tr>\
		<tr>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
			<td><center class='monthly-center'><input class='monthly-btn' type='button' value=''  onClick='monthlyBtn(this.id)'></center></td>\
		</tr>\
	</tbody>\
</table>";
	document.write(tableHtml);
}
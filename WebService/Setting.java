package main;

public class Setting {

	private String nameOfSetting;
	private String valueOfSetting;
	
	public Setting(String nameOfSetting, String valueOfSetting){
		setNameOfSetting(nameOfSetting);
		setValueOfSetting(valueOfSetting);
	}
	
	public String getNameOfSetting() {
		return nameOfSetting;
	}
	public void setNameOfSetting(String nameOfSetting) {
		this.nameOfSetting = nameOfSetting;
	}
	public String getValueOfSetting() {
		return valueOfSetting;
	}
	public void setValueOfSetting(String valueOfSetting) {
		this.valueOfSetting = valueOfSetting;
	}
	
	@Override public String toString(){
		return this.nameOfSetting + " = " + this.valueOfSetting;
	}
	
	
}

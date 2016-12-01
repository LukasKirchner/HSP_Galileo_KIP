package main;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class FileReaderHelper {
	
	public static List<Setting> readFile(File file){
		
		List<Setting> settings = new ArrayList<Setting>(); 
		
		try (BufferedReader br = new BufferedReader(new FileReader(file))) {
	    	String line;
	    	while ((line = br.readLine()) != null) {
	    		if(!line.contains("[")){ 
	       			String[] split = line.split("=");
	       			settings.add(new Setting(split[0].trim(), split[1].trim()));
	    		}
	    	}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return settings;
	}

}

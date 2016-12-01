package main;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URL;
import java.util.List;

public class FileWriterHelper {
	
	public static <T> void writeListToFile(List<T> list, File file){
		
		try {
		    BufferedWriter out = new BufferedWriter(new FileWriter(file));
		    for(T l : list){
		    	out.write(l.toString());
		    	out.newLine();
		    }
		    out.close();
		} catch (IOException e) {
		    System.out.println(e);
		} 
		
	}

}

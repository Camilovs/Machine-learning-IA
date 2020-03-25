package csvreader;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class CSVReader {
    
    BufferedReader br=null;
    String line = "";
    String cvsSplitBy=";";
    String csvFile;
    double[][] dataSet;
    //String csvFile="winequality-red";
    
    public CSVReader(String nameFile){
        this.csvFile =  nameFile;
        dataSet = new double[1600][12];
        read();
    }
    private void read() {     
        try {
            br = new BufferedReader(new FileReader(csvFile));
            while ((line = br.readLine()) != null) {
                
                // use comma as separator
                String[] dataLine = line.split(cvsSplitBy);
                for (String data : dataLine) {
                    if(isNumeric(data))
                }
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }
    private static boolean isNumeric(String cadena){
	try {
		Integer.parseInt(cadena);
		return true;
	} catch (NumberFormatException nfe){
		return false;
	}
}

}

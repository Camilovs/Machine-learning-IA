package csvreader;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import ml_wine.DataSet;

public class CSVReader {
    
    BufferedReader br=null;
    String line = "";
    String cvsSplitBy=";";
    String csvFile;
    DataSet dataSet;
   
    
    public CSVReader(String nameFile){
        this.csvFile =  nameFile;
        dataSet = new DataSet(1600, 12);      
        read();
    }
    private void read() {     
        try {
            br = new BufferedReader(new FileReader(csvFile));
            int j = 0;
            while ((line = br.readLine()) != null) {
                //separador ; de cada dato
                String[] dataLine = line.split(cvsSplitBy);           
                for (int i = 0; i < dataLine.length; i++) {
                    
                    //me aseguro que dato sea un numero, evitando encabezados o cosas raras
                    if(isNumeric(dataLine[i])){
                        dataSet.addData(j, i, Double.parseDouble(dataLine[i]));
                        System.out.println("guardando.."+dataLine[i]);                                                   
                    }                  
                }             
                j++;                  
            }
            
            dataSet.printDataSet();

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
    private boolean isNumeric(String cadena){
	try {
		Double.parseDouble(cadena);
		return true;
	} catch (NumberFormatException x){
		return false;
	}
    }
     
}

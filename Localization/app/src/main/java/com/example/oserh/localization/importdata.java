package com.example.oserh.localization;

import android.content.Context;
import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class importdata{
    public static Context mCtx;
    public static String[] apload(int numTypes,Context context){
        mCtx = context;
        String[] apTable = new String[numTypes];
        try{
            InputStreamReader fileReader = new InputStreamReader(mCtx.getAssets().open("topap.txt"));
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line = null;
            int i=0;
            while((line = bufferedReader.readLine())!=null){
                apTable[i] = line;
                i++;
            }
            bufferedReader.close();
        }catch(IOException ex){
            Log.w("error",ex.toString());
        }
        return apTable;
    }

    public static float[][] fileload(int cellNum,String fileName, Context context){
        mCtx = context;
        int rssSize = 256;
        float[][] rssTable = new float[cellNum][rssSize];
        try{
            InputStreamReader fileReader = new InputStreamReader(mCtx.getAssets().open(fileName));
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line = null;
            int cellIndex = 0;
            while((line = bufferedReader.readLine())!=null){
                String[] lineSplit = line.split(",");
                for(int i=0; i<rssSize; i++)
                {
                    rssTable[cellIndex][i] = Float.parseFloat(lineSplit[i]);
                }
                cellIndex++;
            }
            bufferedReader.close();
        }catch(IOException ex){
            System.out.println("error");
        }
        return rssTable;
    }

    }

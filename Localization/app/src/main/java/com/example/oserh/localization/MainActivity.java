package com.example.oserh.localization;

import android.content.Context;
import android.net.wifi.ScanResult;
import android.net.wifi.WifiManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity {
    public WifiManager wifiManager;
    private TextView textRssi;
    Button buttonRssi, buttonExit, buttonStop;
    Timer timer;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textRssi = (TextView) findViewById(R.id.textRSSI);
        buttonRssi = (Button) findViewById(R.id.buttonRSSI);
        buttonRssi.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (timer != null) {
                    timer.cancel();
                }
                timer = new Timer();
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                int types = 30, numCells = 18;
                                String[] ap = importdata.apload(types, getApplicationContext());
                                float[] freq;
                                freq = new float[numCells];
                                for (int l = 0; l < numCells; l++) {
                                    freq[l] = (float) 1 / numCells;
                                }
                                float max_freq = 0;
                                int location = 0, t = 0;
                                double threshold1 = 0.95;
                                int threshold2 = 5;
                                wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
                                while (max_freq <= threshold1 && t <= threshold2 ) {
                                    wifiManager.startScan();
                                    List<ScanResult> scanResult = wifiManager.getScanResults();
                                    int count = 0;
                                    for (int i = 0; i < scanResult.size(); i++) {
                                        for (int j = 0; j < types; j++) {
                                            if (scanResult.get(i).BSSID.equals(ap[j])) {
                                                count += 1;
                                                String f = String.valueOf(j);
                                                String file = "tran" + f + ".csv";
                                                float[][] ap_temp = importdata.fileload(numCells, file, getApplicationContext());
                                                int level = Math.abs(scanResult.get(i).level);
                                                float sum_freq = 0;
                                                for (int k = 0; k < numCells; k++) {
                                                    freq[k] = freq[k] * ap_temp[k][level];
                                                    sum_freq += freq[k];
                                                }
                                                for (int g = 0; g < numCells; g++) {
                                                    freq[g] /= sum_freq;
                                                    if (freq[g] > max_freq) {
                                                        max_freq = freq[g];
                                                        location = g + 1;
                                                    }
                                                }
                                            } else
                                                textRssi.setText("\n\tNo match mac address" + scanResult.get(i).BSSID);
                                        }
                                    }
                                    t++;
                                    if(count < 7){
                                        location = 18;
                                    }
                                }
                                if (t == (threshold2 + 1)  && location != 18)
                                    textRssi.setText("\n\tWaiting......");
                                else
                                    textRssi.setText("\n\tI am in Cell" + location);
                            }
                        });
                    }
                }, 10, 1000);
            }
        });

        buttonStop = (Button) findViewById(R.id.buttonStop);
        buttonStop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bstop();
            }
        });

        buttonExit = (Button) findViewById(R.id.buttonExit);
        buttonExit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bexit();
            }
        });
    }

    public void bstop() {
                if (timer != null) {
                    timer.cancel();
                    timer = null;
                    textRssi.setText("\n\tStop successfully");
                }
            }

    public void bexit() {
                finish();
                System.exit(0);
            }

    // onResume() register the accelerometer for listening the events
    protected void onResume() {
                super.onResume();
            }

    // onPause() unregister the accelerometer for stop listening the events
    protected void onPause() {
                super.onPause();
            }
}




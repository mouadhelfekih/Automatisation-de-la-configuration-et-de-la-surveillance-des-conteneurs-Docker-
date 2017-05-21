import { Response } from '@angular/http';
import { SearchPipe } from './../search.pipe';
import { ChartService } from './chart.service';
import { Component, OnInit, Pipe,Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router'
declare var jQuery:any;


@Component({
  selector: 'my-charts',
  templateUrl: './charts.component.html',
  styleUrls: ['./charts.component.css'],
  providers:[ChartService],
})
export class ChartsComponent implements OnInit{
@Input() user;
@Input() id_conteneur;
chart:{limit:number,por_mem:number,memory_stats:number,cpu_usage:number};
constructor(private _ChartService: ChartService){}
ngOnInit(){
    this.getStats(this.id_conteneur);
    this.getStats(this.id_conteneur);
    this.getStats(this.id_conteneur);
    this.getStats(this.id_conteneur);
    this.getStats(this.id_conteneur);
    this.getStats(this.id_conteneur);

    this.renderChart();
}
getStats(id){
this._ChartService.postStats(this.user,'http://localhost:8000/stats/',id).subscribe(data => this.chart = data,
  () => {},
  () => {this.renderChart();this.data[0].data.push(this.chart.por_mem);this.data[1].data.push(this.chart.cpu_usage);console.log(this.data);
    }
  );
}

sleepFor( sleepDuration ){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){ /* do nothing */ }
}

private data = [
    {
            name: 'Utilisation de mémoire',
            data: []
        },
          {
            name: 'Utilisation du CPU',
            data: []
        }];

  ngAfterViewInit() {
    this.renderChart();
  }

  renderChart(){
    jQuery('#container').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: 'Statistiques'
        },
        subtitle: {
            text: 'Source: thebulletin.metapress.com'
        },
        xAxis: {
            allowDecimals: false,
            labels: {
                formatter: function () {
                    return this.value;
                }
            }
        },
        yAxis: {
            title: {
                text: ''
            },
            labels: {
                formatter: function () {
                    return this.value ;
                }
            }
        },
        tooltip: {
            pointFormat: '{series.name} produced <b>{point.y:,.0f}</b>' +
                   '<br/>warheads in {point.x}'
        },
        plotOptions: {
            area: {
                pointStart: 1940,
                marker: {
                    enabled: false,
                    symbol: 'circle',
                    radius: 2,
                    states: {
                        hover: {
                            enabled: true
                        }
                    }
                }
            }
        },
        series: this.data
    });
  }

}

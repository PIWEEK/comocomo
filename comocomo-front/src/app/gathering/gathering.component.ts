import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-gathering',
  templateUrl: './gathering.component.html',
  styleUrls: ['./gathering.component.less']
})
export class GatheringComponent implements OnInit {

  constructor(
    private router: Router
  ) { }


  ngOnInit() {
  }

  public onBackClicked() {
    this.router.navigate(['/week']);
  }
}

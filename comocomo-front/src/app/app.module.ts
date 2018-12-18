import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { WeekComponent } from './week/week.component';
import { DayComponent } from './day/day.component';
import { BarnsComponent } from './barns/barns.component';
import { GatheringComponent } from './gathering/gathering.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    WeekComponent,
    DayComponent,
    BarnsComponent,
    GatheringComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

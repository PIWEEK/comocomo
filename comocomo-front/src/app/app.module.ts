import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SvgSpriteComponent } from './shared/svg-sprite/svg-sprite.component';
import { LoginComponent } from './login/login.component';
import { WeekComponent } from './week/week.component';
// import { DayComponent } from './day/day.component';
import { BarnsComponent } from './barns/barns.component';
import { GatheringComponent } from './gathering/gathering.component';
import { MenuBarComponent } from './shared/menu-bar-component/menu-bar.component';
import { NavBarComponent } from './shared/nav-bar-component/nav-bar.component';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    SvgSpriteComponent,
    LoginComponent,
    WeekComponent,
    // DayComponent,
    BarnsComponent,
    GatheringComponent,
    MenuBarComponent,
    NavBarComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    ReactiveFormsModule,
    NgxChartsModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

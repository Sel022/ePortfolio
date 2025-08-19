
import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TripService {
  private baseUrl = '/api/trips';

  constructor(private http: HttpClient) {}

  getTrips(page: number = 1, limit: number = 10): Observable<any> {
    let params = new HttpParams().set('page', page).set('limit', limit);
    return this.http.get(this.baseUrl, { params });
  }

  addTrip(trip: any): Observable<any> {
    return this.http.post(this.baseUrl, trip);
  }

  editTrip(id: string, trip: any): Observable<any> {
    return this.http.put(`${this.baseUrl}/${id}`, trip);
  }

  deleteTrip(id: string): Observable<any> {
    return this.http.delete(`${this.baseUrl}/${id}`);
  }
}


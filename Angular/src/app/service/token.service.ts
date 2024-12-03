import { Injectable } from '@angular/core';
import {setCookie, getCookie, removeCookie} from 'typescript-cookie'
import jwt_decoded, { JwtPayload } from 'jwt-decode';

interface Jwt extends JwtPayload {
  is_admin: boolean
}
@Injectable({
  providedIn: 'root'
})
export class TokenService {

  constructor() { }

  createToken(token: string) {
    setCookie('token', token, {expires:365, path:"/"})
  }

  getToken() {
    const token = getCookie('token');
    return token;
  }

  removeToken() {
    removeCookie('token')
  }

  isValidToken() {
    const token = this.getToken()
    if(!token){
      return false
    }
    const decodeToken = jwt_decoded<JwtPayload>(token)
    console.log(decodeToken)
    if(decodeToken && decodeToken.exp){
      const tokenDate = new Date(0);
      tokenDate.setUTCSeconds(decodeToken.exp)
      const today = new Date()
      return tokenDate.getTime() > today.getTime()
    }
    return false
  }

  isAdmin() {
    const token = this.getToken()
    if(!token){
      return false
    }
    const decodeToken = jwt_decoded<Jwt>(token)

    if(decodeToken && decodeToken.is_admin){
      return true
    }
    return false
  }
}

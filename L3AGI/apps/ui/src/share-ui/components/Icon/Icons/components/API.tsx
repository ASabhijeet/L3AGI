/* eslint-disable */
/* tslint:disable */
import * as React from 'react';
export interface APIProps extends React.SVGAttributes<SVGElement> {
size?: string | number;
}
const API: React.FC<APIProps> = ({size, ...props}) => (
  <svg viewBox="0 0 40 40" fill="currentColor" width={ size || "40" } height={ size || "40" } {...props}>
    <path d="M10 30.2714C10 31.2593 10.2372 31.8501 11.1402 32.2973C13.1631 33.1983 15.9709 33.7809 19.281 33.7809C22.6741 33.7809 26.4604 33.2613 29.1025 31.9807C30.572 31.2853 30.9498 30.6199 30.9498 29.0845V11.1722C30.9498 9.16406 30.0344 8.22305 28.0987 8.22305H26.9992V7.81757C26.9992 6.59625 26.3394 6 25.2428 6C24.8617 6 24.4124 6.08203 23.8916 6.25242C20.3652 7.39781 17.1203 8.15719 13.0098 8.15719H12.1145C10.7582 8.15719 10 8.92711 10 10.1684V30.2714ZM14.3205 17.3142V13.3005C14.3205 13.1344 14.4419 12.9937 14.608 12.982C17.3132 12.8681 19.7465 12.4362 22.2637 11.5031C22.4043 11.4445 22.6525 11.5031 22.6525 11.7865V15.9633C22.6525 16.0687 22.5939 16.1763 22.4863 16.2136C20.2898 17.1105 17.4123 17.5955 14.608 17.5976C14.4536 17.5976 14.3205 17.5017 14.3205 17.3142ZM16.1141 31.467C20.2935 31.3001 24.033 30.1502 26.098 28.5769C26.7362 28.0908 27.0013 27.5993 27.0013 26.5153V10.4198H28.0534C28.5205 10.4198 28.753 10.6694 28.753 11.1975V28.8523C28.753 29.5448 28.637 29.8322 27.9648 30.123C25.8332 31.0519 22.9021 31.6491 20.1163 31.6765C18.7789 31.6913 17.4983 31.6282 16.1141 31.467Z"
      fill="#fff" />
  </svg>
);
API.displayName = 'API';
export default API;
/* tslint:enable */
/* eslint-enable */
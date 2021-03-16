import { Laptime } from "./laptime"

export class Circuit {
    constructor(
        public name: string,
        public laptime: Laptime,
        public fuelPerLap: number
    ) {}
}

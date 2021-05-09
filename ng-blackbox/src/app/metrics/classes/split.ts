export class Split {
  circuit: string;
  rookie: number;
  am: number;
  silver: number;
  pro: number;

  constructor(circuit, pro, silver, am, rookie) {
    this.circuit = circuit;
    this.rookie = this.parseSplit(rookie);
    this.am = this.parseSplit(am);
    this.silver = this.parseSplit(silver);
    this.pro = this.parseSplit(pro);
  }

  private parseSplit(time): number {
    const regex = /(?<minutes>[0-9]+):(?<seconds>[0-9]+)\.(?<milliseconds>[0-9]+)/;
    const groups = time.match(regex).groups;

    return (
      (parseInt(groups.minutes, 10) * 60 + parseInt(groups.seconds)) * 1000 +
      parseInt(groups.milliseconds, 10)
    );
  }

  getSplit(time) {
    if (time < this.pro) {
      return 'pro';
    } else if (time <= this.silver) {
      return 'silver';
    } else if (time <= this.am) {
      return 'am';
    } else {
      return 'rookie';
    }
  }
}

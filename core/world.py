@dataclass
class World:

    clock: GameClock

    pitch: Pitch

    ball: Ball

    home: Team

    away: Team

    score: Score

    current_moment: FootballMoment

    momentum: Momentum

    commentary: str

    state: MatchState

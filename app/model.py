from peewee import *

database = MySQLDatabase('faf_lobby', **{'user': 'root', 'password': 'test1234'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class AiNames(BaseModel):
    login = CharField(unique=True)

    class Meta:
        db_table = 'AI_names'

class AiRating(BaseModel):
    deviation = FloatField(null=True)
    id = ForeignKeyField(db_column='id', primary_key=True, rel_model=AiNames, to_field='id')
    mean = FloatField(null=True)
    numgames = IntegerField(db_column='numGames')

    class Meta:
        db_table = 'AI_rating'

class AuthGroup(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(BaseModel):
    group = IntegerField(db_column='group_id', index=True)
    permission = IntegerField(db_column='permission_id', index=True)

    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(BaseModel):
    codename = CharField()
    content_type = IntegerField(db_column='content_type_id', index=True)
    name = CharField()

    class Meta:
        db_table = 'auth_permission'

class AuthUser(BaseModel):
    date_joined = DateTimeField()
    email = CharField()
    first_name = CharField()
    is_active = IntegerField()
    is_staff = IntegerField()
    is_superuser = IntegerField()
    last_login = DateTimeField()
    last_name = CharField()
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(BaseModel):
    group = IntegerField(db_column='group_id', index=True)
    user = IntegerField(db_column='user_id', index=True)

    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(BaseModel):
    permission = IntegerField(db_column='permission_id', index=True)
    user = IntegerField(db_column='user_id', index=True)

    class Meta:
        db_table = 'auth_user_user_permissions'

class Login(BaseModel):
    email = CharField(null=True, unique=True)
    ip = CharField(null=True)
    laddercancelled = IntegerField(db_column='ladderCancelled')
    login = CharField(unique=True)
    password = CharField()
    session = IntegerField()
    steamchecked = IntegerField()
    steamid = BigIntegerField(null=True, unique=True)
    uniqueid = CharField(db_column='uniqueId', null=True, unique=True)
    validated = IntegerField()

    class Meta:
        db_table = 'login'

class AvatarsList(BaseModel):
    tooltip = CharField(null=True)
    url = CharField()

    class Meta:
        db_table = 'avatars_list'

class Avatars(BaseModel):
    idavatar = ForeignKeyField(db_column='idAvatar', rel_model=AvatarsList, to_field='id')
    iduser = ForeignKeyField(db_column='idUser', rel_model=Login, to_field='id')
    selected = IntegerField()

    class Meta:
        db_table = 'avatars'

class Bet(BaseModel):
    amount = IntegerField()
    userid = PrimaryKeyField()

    class Meta:
        db_table = 'bet'

class CoopLeaderboard(BaseModel):
    gameuid = BigIntegerField(unique=True)
    mission = IntegerField()
    secondary = IntegerField()
    time = TimeField()

    class Meta:
        db_table = 'coop_leaderboard'

class CoopMap(BaseModel):
    description = TextField(null=True)
    filename = CharField(index=True, null=True)
    name = CharField(null=True)
    type = IntegerField()
    version = DecimalField(null=True)

    class Meta:
        db_table = 'coop_map'

class GameFeaturedmods(BaseModel):
    description = TextField()
    gamemod = CharField(null=True)
    name = CharField()
    publish = IntegerField()

    class Meta:
        db_table = 'game_featuredMods'

class FeaturedModsOwners(BaseModel):
    moduid = ForeignKeyField(db_column='moduid', rel_model=GameFeaturedmods, to_field='id')
    uid = ForeignKeyField(db_column='uid', rel_model=Login, to_field='id')

    class Meta:
        db_table = 'featured_mods_owners'

class Foes(BaseModel):
    idfoe = ForeignKeyField(db_column='idFoe', rel_model=Login, to_field='id')
    iduser = ForeignKeyField(db_column='idUser', rel_model=Login, related_name='login_iduser_set', to_field='id')

    class Meta:
        db_table = 'foes'

class Friends(BaseModel):
    idfriend = ForeignKeyField(db_column='idFriend', rel_model=Login, to_field='id')
    iduser = ForeignKeyField(db_column='idUser', rel_model=Login, related_name='login_iduser_set', to_field='id')

    class Meta:
        db_table = 'friends'

class TableMap(BaseModel):
    battle_type = CharField(null=True)
    description = TextField(null=True)
    filename = CharField(index=True, null=True)
    hidden = IntegerField()
    map_sizex = DecimalField(db_column='map_sizeX', null=True)
    map_sizey = DecimalField(db_column='map_sizeY', null=True)
    map_type = CharField(null=True)
    mapuid = IntegerField(index=True)
    max_players = DecimalField(null=True)
    name = CharField(null=True)
    version = DecimalField(null=True)

    class Meta:
        db_table = 'table_map'

class GameStatsBak(BaseModel):
    endtime = DateTimeField(db_column='EndTime', index=True, null=True)
    gamemod = ForeignKeyField(db_column='gameMod', null=True, rel_model=GameFeaturedmods, to_field='id')
    gamename = TextField(db_column='gameName', null=True)
    gametype = CharField(db_column='gameType', null=True)
    host = ForeignKeyField(db_column='host', null=True, rel_model=Login, to_field='id')
    id = BigIntegerField(primary_key=True)
    mapid = ForeignKeyField(db_column='mapId', null=True, rel_model=TableMap, to_field='id')
    starttime = DateTimeField(db_column='startTime', index=True, null=True)
    valid = IntegerField()

    class Meta:
        db_table = 'game_stats_bak'

class GameMinRating(BaseModel):
    id = ForeignKeyField(db_column='id', primary_key=True, rel_model=GameStatsBak, to_field='id')
    minrating = FloatField(db_column='minRating', null=True)

    class Meta:
        db_table = 'game_min_rating'

class GamePlayerStats(BaseModel):
    ai = IntegerField(db_column='AI')
    after_deviation = FloatField(null=True)
    after_mean = FloatField(null=True)
    color = IntegerField()
    deviation = FloatField()
    faction = IntegerField()
    gameid = BigIntegerField(db_column='gameId', index=True)
    id = BigIntegerField(primary_key=True)
    mean = FloatField()
    place = IntegerField()
    playerid = IntegerField(db_column='playerId', index=True)
    score = IntegerField()
    scoretime = DateTimeField(db_column='scoreTime', null=True)
    team = IntegerField()

    class Meta:
        db_table = 'game_player_stats'

class GamePlayerStatsBak(BaseModel):
    ai = IntegerField(db_column='AI')
    after_deviation = FloatField(null=True)
    after_mean = FloatField(null=True)
    color = IntegerField()
    deviation = FloatField()
    faction = IntegerField()
    gameid = ForeignKeyField(db_column='gameId', rel_model=GameStatsBak, to_field='id')
    id = BigIntegerField(primary_key=True)
    mean = FloatField()
    place = IntegerField()
    playerid = ForeignKeyField(db_column='playerId', rel_model=Login, to_field='id')
    score = IntegerField()
    scoretime = DateTimeField(db_column='scoreTime', null=True)
    team = IntegerField()

    class Meta:
        db_table = 'game_player_stats_bak'

class GameReplays(BaseModel):
    uid = BigIntegerField(db_column='UID', primary_key=True)
    file = TextField()

    class Meta:
        db_table = 'game_replays'

class GameReplaysOld(BaseModel):
    uid = ForeignKeyField(db_column='UID', primary_key=True, rel_model=GameStatsBak, to_field='id')
    file = TextField()

    class Meta:
        db_table = 'game_replays_old'

class GameStats(BaseModel):
    endtime = DateTimeField(db_column='EndTime', null=True)
    gamemod = IntegerField(db_column='gameMod', null=True)
    gamename = TextField(db_column='gameName', null=True)
    gametype = CharField(db_column='gameType', null=True)
    host = IntegerField(null=True)
    id = BigIntegerField(primary_key=True)
    mapid = IntegerField(db_column='mapId', null=True)
    starttime = DateTimeField(db_column='startTime', index=True, null=True)

    class Meta:
        db_table = 'game_stats'

class GlobalRating(BaseModel):
    deviation = FloatField(null=True)
    id = ForeignKeyField(db_column='id', primary_key=True, rel_model=Login, related_name='login_id_set', to_field='id')
    is_active = IntegerField()
    mean = FloatField(null=True)
    numgames = IntegerField(db_column='numGames')

    class Meta:
        db_table = 'global_rating'

class Ladder1V1Rating(BaseModel):
    deviation = FloatField(null=True)
    id = ForeignKeyField(db_column='id', primary_key=True, rel_model=Login, to_field='id')
    is_active = IntegerField()
    mean = FloatField(null=True)
    numgames = IntegerField(db_column='numGames')
    wingames = IntegerField(db_column='winGames')

    class Meta:
        db_table = 'ladder1v1_rating'

class LadderDivision(BaseModel):
    league = IntegerField()
    limit = IntegerField()
    name = CharField(unique=True)

    class Meta:
        db_table = 'ladder_division'

class LadderDivisions(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'ladder_divisions'

class LadderMap(BaseModel):
    idmap = ForeignKeyField(db_column='idmap', rel_model=TableMap, to_field='id', unique=True)

    class Meta:
        db_table = 'ladder_map'

class LadderMapSelection(BaseModel):
    idmap = IntegerField(db_column='idMap', index=True)
    iduser = IntegerField(db_column='idUser')

    class Meta:
        db_table = 'ladder_map_selection'

class LadderSeason1(BaseModel):
    division = IntegerField()
    iduser = IntegerField(db_column='idUser', unique=True)
    league = IntegerField()
    score = IntegerField()

    class Meta:
        db_table = 'ladder_season_1'

class LadderSeason2(BaseModel):
    division = IntegerField()
    iduser = IntegerField(db_column='idUser', unique=True)
    league = IntegerField()
    score = IntegerField()

    class Meta:
        db_table = 'ladder_season_2'

class LadderSeason3(BaseModel):
    division = IntegerField(index=True)
    iduser = IntegerField(db_column='idUser', unique=True)
    league = IntegerField(index=True)
    score = IntegerField()

    class Meta:
        db_table = 'ladder_season_3'

class LadderSeason3Safe(BaseModel):
    division = IntegerField(index=True)
    iduser = IntegerField(db_column='idUser', unique=True)
    league = IntegerField(index=True)
    score = IntegerField()

    class Meta:
        db_table = 'ladder_season_3_safe'

class LadderSeason4(BaseModel):
    division = IntegerField(index=True)
    iduser = IntegerField(db_column='idUser', unique=True)
    league = IntegerField(index=True)
    score = IntegerField()

    class Meta:
        db_table = 'ladder_season_4'

class LadderSeason5(BaseModel):
    iduser = IntegerField(db_column='idUser', unique=True)
    league = IntegerField(index=True)
    score = FloatField()

    class Meta:
        db_table = 'ladder_season_5'

class LobbyAdmin(BaseModel):
    group = IntegerField()
    user = PrimaryKeyField(db_column='user_id')

    class Meta:
        db_table = 'lobby_admin'

class LobbyBan(BaseModel):
    iduser = ForeignKeyField(db_column='idUser', null=True, rel_model=Login, to_field='id', unique=True)
    reason = CharField()

    class Meta:
        db_table = 'lobby_ban'

class MatchmakerBan(BaseModel):
    userid = IntegerField()

    class Meta:
        db_table = 'matchmaker_ban'

class NameHistory(BaseModel):
    change_time = DateTimeField(primary_key=True)
    previous_name = CharField()
    user = ForeignKeyField(db_column='user_id', rel_model=Login, to_field='id')

    class Meta:
        db_table = 'name_history'

class NomadsBeta(BaseModel):
    iduser = ForeignKeyField(db_column='idUser', null=True, rel_model=Login, to_field='id', unique=True)

    class Meta:
        db_table = 'nomads_beta'

class PatchsTable(BaseModel):
    frommd5 = CharField(db_column='fromMd5', null=True)
    idpatchs_table = PrimaryKeyField()
    patchfile = CharField(db_column='patchFile', null=True)
    tomd5 = CharField(db_column='toMd5', null=True)

    class Meta:
        db_table = 'patchs_table'

class RecoveryemailsEnc(BaseModel):
    id = BigIntegerField(db_column='ID', primary_key=True)
    key = CharField(db_column='Key')
    userid = ForeignKeyField(db_column='UserID', rel_model=Login, to_field='id')
    expdate = DateTimeField(db_column='expDate')

    class Meta:
        db_table = 'recoveryemails_enc'

class SubmittedReplays(BaseModel):
    experted_by = ForeignKeyField(db_column='experted_by', null=True, rel_model=Login, to_field='id')
    featured_by = ForeignKeyField(db_column='featured_by', null=True, rel_model=Login, related_name='login_featured_by_set', to_field='id')
    game = ForeignKeyField(db_column='game_id', primary_key=True, rel_model=GameStatsBak, to_field='id')
    rating = DecimalField(null=True)
    reserved_by = IntegerField(index=True, null=True)
    voters = TextField(null=True)
    votes = IntegerField()

    class Meta:
        db_table = 'submitted_replays'

class ReplayComment(BaseModel):
    replay = ForeignKeyField(db_column='replay_id', rel_model=SubmittedReplays, to_field='game')
    text = TextField()
    timestamp = DateTimeField()
    user = ForeignKeyField(db_column='user_id', rel_model=Login, to_field='id')

    class Meta:
        db_table = 'replay_comment'

class ReplayReview(BaseModel):
    body = TextField()
    submitted_replay = ForeignKeyField(db_column='submitted_replay_id', rel_model=SubmittedReplays, to_field='game')
    type = CharField()
    user = ForeignKeyField(db_column='user_id', rel_model=Login, to_field='id')

    class Meta:
        db_table = 'replay_review'

class ReplayVault(BaseModel):
    endtime = DateTimeField(db_column='EndTime', null=True)
    filename = CharField(null=True)
    gamename = TextField(db_column='gameName', null=True)
    gamemod = CharField(index=True, null=True)
    gamemodid = IntegerField(null=True)
    id = BigIntegerField(index=True)
    mapid = IntegerField(db_column='mapId', index=True, null=True)
    playerid = IntegerField(db_column='playerId', index=True)
    rating = FloatField(index=True)
    starttime = DateTimeField(db_column='startTime', index=True, null=True)

    class Meta:
        db_table = 'replay_vault'

class SearchPlayer(BaseModel):
    id = BigIntegerField()
    playerid = IntegerField()

    class Meta:
        db_table = 'search_player'

class SmurfTable(BaseModel):
    origid = ForeignKeyField(db_column='origId', rel_model=Login, to_field='id')
    smurfid = ForeignKeyField(db_column='smurfId', rel_model=Login, related_name='login_smurfid_set', to_field='id')

    class Meta:
        db_table = 'smurf_table'

class SteamLinkRequest(BaseModel):
    key = CharField(db_column='Key')
    expdate = DateTimeField(db_column='expDate')
    uid = IntegerField()

    class Meta:
        db_table = 'steam_link_request'

class SteamUniqueid(BaseModel):
    uniqueid = CharField(unique=True)

    class Meta:
        db_table = 'steam_uniqueid'

class SwissTournaments(BaseModel):
    description = CharField(null=True)
    host = ForeignKeyField(db_column='host', null=True, rel_model=Login, to_field='id')
    maxplayers = IntegerField(null=True)
    maxrating = IntegerField(null=True)
    minplayers = IntegerField(null=True)
    minrating = IntegerField(null=True)
    name = CharField()
    tourney_date = DateTimeField(null=True)
    tourney_state = IntegerField(null=True)

    class Meta:
        db_table = 'swiss_tournaments'

class SwissTournamentsPlayers(BaseModel):
    idtourney = ForeignKeyField(db_column='idtourney', rel_model=SwissTournaments, to_field='id')
    iduser = ForeignKeyField(db_column='iduser', rel_model=Login, to_field='id')

    class Meta:
        db_table = 'swiss_tournaments_players'

class TableMapBroken(BaseModel):
    approved = IntegerField()
    broken = PrimaryKeyField(db_column='broken_id')
    description = TextField()
    map = ForeignKeyField(db_column='map_id', rel_model=TableMap, to_field='id')
    user = ForeignKeyField(db_column='user_id', null=True, rel_model=Login, to_field='id')

    class Meta:
        db_table = 'table_map_broken'

class TableMapComments(BaseModel):
    comment_date = DateTimeField()
    comment = PrimaryKeyField(db_column='comment_id')
    comment_text = TextField()
    map = ForeignKeyField(db_column='map_id', rel_model=TableMap, to_field='id')
    user = ForeignKeyField(db_column='user_id', rel_model=Login, to_field='id')

    class Meta:
        db_table = 'table_map_comments'

class TableMapFeatures(BaseModel):
    downloads = IntegerField()
    map = ForeignKeyField(db_column='map_id', primary_key=True, rel_model=TableMap, to_field='id')
    num_draws = IntegerField()
    rating = FloatField()
    times_played = IntegerField()
    voters = TextField()

    class Meta:
        db_table = 'table_map_features'

class TableMapUnranked(BaseModel):

    class Meta:
        db_table = 'table_map_unranked'

class TableMapUploaders(BaseModel):
    mapid = ForeignKeyField(db_column='mapid', rel_model=TableMap, to_field='id', unique=True)
    userid = ForeignKeyField(db_column='userid', rel_model=Login, to_field='id')

    class Meta:
        db_table = 'table_map_uploaders'

class TableMod(BaseModel):
    author = CharField()
    big = IntegerField()
    date = DateTimeField()
    description = CharField()
    downloads = IntegerField()
    filename = CharField()
    icon = CharField()
    likers = TextField()
    likes = IntegerField()
    name = CharField()
    played = IntegerField()
    ranked = IntegerField()
    small = IntegerField()
    ui = IntegerField()
    uid = CharField(unique=True)
    version = IntegerField()

    class Meta:
        db_table = 'table_mod'

class Test(BaseModel):
    file = TextField()
    id = IntegerField()

    class Meta:
        db_table = 'test'

class Test2(BaseModel):
    id = IntegerField()
    test = IntegerField()

    class Meta:
        db_table = 'test2'

class TestGameReplays(BaseModel):
    uid = BigIntegerField(db_column='UID', primary_key=True)
    file = TextField()

    class Meta:
        db_table = 'test_game_replays'

class TutorialSections(BaseModel):
    description = CharField()
    section = CharField()

    class Meta:
        db_table = 'tutorial_sections'

class Tutorials(BaseModel):
    description = CharField()
    map = CharField()
    name = CharField()
    section = ForeignKeyField(db_column='section', rel_model=TutorialSections, to_field='id')
    url = CharField()

    class Meta:
        db_table = 'tutorials'

class Uniqueid(BaseModel):
    smbiosbiosversion = CharField(db_column='SMBIOSBIOSVersion')
    deviceid = CharField(db_column='deviceID')
    manufacturer = CharField()
    mem_serialnumber = CharField(db_column='mem_SerialNumber')
    name = CharField()
    processorid = CharField(db_column='processorId')
    serialnumber = CharField(db_column='serialNumber')
    userid = ForeignKeyField(db_column='userid', rel_model=Login, to_field='id')
    uuid = CharField()
    volumeserialnumber = CharField(db_column='volumeSerialNumber')

    class Meta:
        db_table = 'uniqueid'

class Updates(BaseModel):
    file = CharField(null=True)
    md5 = CharField(null=True)

    class Meta:
        db_table = 'updates'

class UpdatesBalancetesting(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_balancetesting'

class UpdatesBalancetestingFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_balancetesting_files'

class UpdatesBlackops(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_blackops'

class UpdatesBlackopsFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_blackops_files'

class UpdatesCivilians(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_civilians'

class UpdatesCiviliansFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_civilians_files'

class UpdatesClaustrophobia(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_claustrophobia'

class UpdatesClaustrophobiaFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_claustrophobia_files'

class UpdatesCoop(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_coop'

class UpdatesCoopFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_coop_files'

class UpdatesDiamond(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_diamond'

class UpdatesDiamondFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_diamond_files'

class UpdatesEngyredesign(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_engyredesign'

class UpdatesEngyredesignFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_engyredesign_files'

class UpdatesFaf(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_faf'

class UpdatesFafFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_faf_files'

class UpdatesGw(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_gw'

class UpdatesGwFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_gw_files'

class UpdatesKoth(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_koth'

class UpdatesKothFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_koth_files'

class UpdatesLabwars(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_labwars'

class UpdatesLabwarsFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_labwars_files'

class UpdatesMatchmaker(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_matchmaker'

class UpdatesMatchmakerFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_matchmaker_files'

class UpdatesMurderparty(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_murderparty'

class UpdatesMurderpartyFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_murderparty_files'

class UpdatesNomads(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_nomads'

class UpdatesNomadsFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_nomads_files'

class UpdatesPhantomx(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_phantomx'

class UpdatesPhantomxFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_phantomx_files'

class UpdatesSupremedestruction(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_supremeDestruction'

class UpdatesSupremedestructionFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_supremeDestruction_files'

class UpdatesVanilla(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_vanilla'

class UpdatesVanillaFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_vanilla_files'

class UpdatesWyvern(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_wyvern'

class UpdatesWyvernFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_wyvern_files'

class UpdatesXtremewars(BaseModel):
    filename = CharField()
    id = IntegerField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'updates_xtremewars'

class UpdatesXtremewarsFiles(BaseModel):
    fileid = IntegerField(db_column='fileId', index=True)
    md5 = CharField()
    name = CharField()
    obselete = IntegerField()
    version = IntegerField()

    class Meta:
        db_table = 'updates_xtremewars_files'

class UserAddedReplays(BaseModel):
    game = ForeignKeyField(db_column='game_id', rel_model=GameStatsBak, to_field='id')
    user = ForeignKeyField(db_column='user_id', rel_model=Login, to_field='id')

    class Meta:
        db_table = 'user_added_replays'
        primary_key = CompositeKey('game', 'user')

class UserGroups(BaseModel):
    group = CharField()
    module = CharField()
    user = ForeignKeyField(db_column='user_id', rel_model=Login, to_field='id')

    class Meta:
        db_table = 'user_groups'

class ValidateAccount(BaseModel):
    id = BigIntegerField(db_column='ID', primary_key=True)
    key = CharField(db_column='Key')
    userid = ForeignKeyField(db_column='UserID', rel_model=Login, to_field='id')
    expdate = DateTimeField(db_column='expDate')

    class Meta:
        db_table = 'validate_account'

class VaultAdmin(BaseModel):
    group = IntegerField()
    user = PrimaryKeyField(db_column='user_id')

    class Meta:
        db_table = 'vault_admin'

class VersionLobby(BaseModel):
    file = CharField(null=True)
    version = IntegerField(null=True)

    class Meta:
        db_table = 'version_lobby'

class ViewGlobalRating(BaseModel):
    deviation = FloatField(null=True)
    is_active = IntegerField()
    mean = FloatField(null=True)
    numgames = IntegerField(db_column='numGames')

    class Meta:
        db_table = 'view_global_rating'


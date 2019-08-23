# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TestingClaims(models.Model):
    source = models.TextField(db_column='SOURCE', blank=True, null=True)  # Field name made lowercase.
    sn = models.IntegerField(db_column='SN', blank=True, null=True)  # Field name made lowercase.
    clmnum = models.TextField(db_column='CLMNUM', blank=True, null=True)  # Field name made lowercase.
    claimlinenumber = models.IntegerField(db_column='CLAIMLINENUMBER', blank=True, null=True)  # Field name made lowercase.
    clmtype = models.TextField(db_column='CLMTYPE', blank=True, null=True)  # Field name made lowercase.
    clmtypedesc = models.TextField(db_column='CLMTYPEDESC', blank=True, null=True)  # Field name made lowercase.
    clmcategory = models.TextField(db_column='CLMCATEGORY', blank=True, null=True)  # Field name made lowercase.
    memid = models.IntegerField(db_column='MEMID', blank=True, null=True)  # Field name made lowercase.
    enrid = models.IntegerField(db_column='ENRID', blank=True, null=True)  # Field name made lowercase.
    relflag = models.TextField(db_column='RELFLAG', blank=True, null=True)  # Field name made lowercase.
    memfirstname = models.TextField(db_column='MEMFIRSTNAME', blank=True, null=True)  # Field name made lowercase.
    memlastname = models.TextField(db_column='MEMLASTNAME', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    dob = models.TextField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    addr1 = models.TextField(db_column='ADDR1', blank=True, null=True)  # Field name made lowercase.
    addr2 = models.TextField(db_column='ADDR2', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    homephone = models.TextField(db_column='HOMEPHONE', blank=True, null=True)  # Field name made lowercase.
    workphone = models.TextField(db_column='WORKPHONE', blank=True, null=True)  # Field name made lowercase.
    lvlid1 = models.TextField(db_column='LVLID1', blank=True, null=True)  # Field name made lowercase.
    lvldesc1 = models.TextField(db_column='LVLDESC1', blank=True, null=True)  # Field name made lowercase.
    lvlid2 = models.IntegerField(db_column='LVLID2', blank=True, null=True)  # Field name made lowercase.
    lvldesc2 = models.TextField(db_column='LVLDESC2', blank=True, null=True)  # Field name made lowercase.
    lvlid3 = models.TextField(db_column='LVLID3', blank=True, null=True)  # Field name made lowercase.
    lvldesc3 = models.TextField(db_column='LVLDESC3', blank=True, null=True)  # Field name made lowercase.
    lvlid4 = models.IntegerField(db_column='LVLID4', blank=True, null=True)  # Field name made lowercase.
    lvldesc4 = models.TextField(db_column='LVLDESC4', blank=True, null=True)  # Field name made lowercase.
    lvlid5 = models.TextField(db_column='LVLID5', blank=True, null=True)  # Field name made lowercase.
    lvldesc5 = models.TextField(db_column='LVLDESC5', blank=True, null=True)  # Field name made lowercase.
    lvlid6 = models.TextField(db_column='LVLID6', blank=True, null=True)  # Field name made lowercase.
    lvldesc6 = models.TextField(db_column='LVLDESC6', blank=True, null=True)  # Field name made lowercase.
    lvlid7 = models.TextField(db_column='LVLID7', blank=True, null=True)  # Field name made lowercase.
    lvldesc7 = models.TextField(db_column='LVLDESC7', blank=True, null=True)  # Field name made lowercase.
    lvlid8 = models.TextField(db_column='LVLID8', blank=True, null=True)  # Field name made lowercase.
    lvldesc8 = models.TextField(db_column='LVLDESC8', blank=True, null=True)  # Field name made lowercase.
    lvlid9 = models.TextField(db_column='LVLID9', blank=True, null=True)  # Field name made lowercase.
    lvldesc9 = models.TextField(db_column='LVLDESC9', blank=True, null=True)  # Field name made lowercase.
    lvlid10 = models.TextField(db_column='LVLID10', blank=True, null=True)  # Field name made lowercase.
    lvldesc10 = models.TextField(db_column='LVLDESC10', blank=True, null=True)  # Field name made lowercase.
    fromdate = models.TextField(db_column='FROMDATE', blank=True, null=True)  # Field name made lowercase.
    todate = models.TextField(db_column='TODATE', blank=True, null=True)  # Field name made lowercase.
    servicedate = models.TextField(db_column='SERVICEDATE', blank=True, null=True)  # Field name made lowercase.
    rcvdate = models.TextField(db_column='RCVDATE', blank=True, null=True)  # Field name made lowercase.
    paiddate = models.TextField(db_column='PAIDDATE', blank=True, null=True)  # Field name made lowercase.
    billtype = models.TextField(db_column='BILLTYPE', blank=True, null=True)  # Field name made lowercase.
    poscode = models.IntegerField(db_column='POSCODE', blank=True, null=True)  # Field name made lowercase.
    posdesc = models.TextField(db_column='POSDESC', blank=True, null=True)  # Field name made lowercase.
    speccode = models.TextField(db_column='SPECCODE', blank=True, null=True)  # Field name made lowercase.
    specdesc = models.TextField(db_column='SPECDESC', blank=True, null=True)  # Field name made lowercase.
    diagcode = models.TextField(db_column='DIAGCODE', blank=True, null=True)  # Field name made lowercase.
    diagdesc = models.TextField(db_column='DIAGDESC', blank=True, null=True)  # Field name made lowercase.
    firstdiagcode = models.TextField(db_column='FIRSTDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    firstdiagdesc = models.TextField(db_column='FIRSTDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    seconddiagcode = models.TextField(db_column='SECONDDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    seconddiagdesc = models.TextField(db_column='SECONDDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    thirddiagcode = models.TextField(db_column='THIRDDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    thirddiagdesc = models.TextField(db_column='THIRDDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    fourthdiagcode = models.TextField(db_column='FOURTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    fourthdiagdesc = models.TextField(db_column='FOURTHDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    fifthdiagcode = models.TextField(db_column='FIFTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    fifthdiagdesc = models.TextField(db_column='FIFTHDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    sixthdiagcode = models.TextField(db_column='SIXTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    sixthdiagdesc = models.TextField(db_column='SIXTHDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    seventhdiagcode = models.TextField(db_column='SEVENTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    seventhdiagdesc = models.TextField(db_column='SEVENTHDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    eighthdiagcode = models.TextField(db_column='EIGHTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    eighthdiagdesc = models.TextField(db_column='EIGHTHDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    ninthdiagcode = models.TextField(db_column='NINTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    ninthdiagdesc = models.TextField(db_column='NINTHDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    tenthdiagcode = models.TextField(db_column='TENTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    tenthdiagdesc = models.TextField(db_column='TENTHDIAGDESC', blank=True, null=True)  # Field name made lowercase.
    proctype = models.TextField(db_column='PROCTYPE', blank=True, null=True)  # Field name made lowercase.
    proccode = models.TextField(db_column='PROCCODE', blank=True, null=True)  # Field name made lowercase.
    procdesc = models.TextField(db_column='PROCDESC', blank=True, null=True)  # Field name made lowercase.
    revcode = models.TextField(db_column='REVCODE', blank=True, null=True)  # Field name made lowercase.
    drgcode = models.TextField(db_column='DRGCODE', blank=True, null=True)  # Field name made lowercase.
    modifiercode = models.TextField(db_column='MODIFIERCODE', blank=True, null=True)  # Field name made lowercase.
    modifierdesc = models.TextField(db_column='MODIFIERDESC', blank=True, null=True)  # Field name made lowercase.
    cpt4_1 = models.TextField(db_column='CPT4_1', blank=True, null=True)  # Field name made lowercase.
    cpt4_2 = models.TextField(db_column='CPT4_2', blank=True, null=True)  # Field name made lowercase.
    cpt4_3 = models.TextField(db_column='CPT4_3', blank=True, null=True)  # Field name made lowercase.
    hcpcs = models.TextField(db_column='HCPCS', blank=True, null=True)  # Field name made lowercase.
    cptii = models.TextField(db_column='CPTII', blank=True, null=True)  # Field name made lowercase.
    modifiercode2 = models.TextField(db_column='MODIFIERCODE2', blank=True, null=True)  # Field name made lowercase.
    revcode1 = models.TextField(db_column='REVCODE1', blank=True, null=True)  # Field name made lowercase.
    revcode2 = models.TextField(db_column='REVCODE2', blank=True, null=True)  # Field name made lowercase.
    revcode4 = models.TextField(db_column='REVCODE4', blank=True, null=True)  # Field name made lowercase.
    revcode3 = models.TextField(db_column='REVCODE3', blank=True, null=True)  # Field name made lowercase.
    revcode5 = models.TextField(db_column='REVCODE5', blank=True, null=True)  # Field name made lowercase.
    icd9proccode1 = models.TextField(db_column='ICD9PROCCODE1', blank=True, null=True)  # Field name made lowercase.
    icd9proccode2 = models.TextField(db_column='ICD9PROCCODE2', blank=True, null=True)  # Field name made lowercase.
    icd9proccode3 = models.TextField(db_column='ICD9PROCCODE3', blank=True, null=True)  # Field name made lowercase.
    icd9proccode4 = models.TextField(db_column='ICD9PROCCODE4', blank=True, null=True)  # Field name made lowercase.
    icd9proccode5 = models.TextField(db_column='ICD9PROCCODE5', blank=True, null=True)  # Field name made lowercase.
    icd9proccode6 = models.TextField(db_column='ICD9PROCCODE6', blank=True, null=True)  # Field name made lowercase.
    drgtype = models.TextField(db_column='DRGTYPE', blank=True, null=True)  # Field name made lowercase.
    drgidentifier = models.TextField(db_column='DRGIDENTIFIER', blank=True, null=True)  # Field name made lowercase.
    ipdays = models.IntegerField(db_column='IPDAYS', blank=True, null=True)  # Field name made lowercase.
    dischstatus = models.TextField(db_column='DISCHSTATUS', blank=True, null=True)  # Field name made lowercase.
    typeofbill = models.TextField(db_column='TYPEOFBILL', blank=True, null=True)  # Field name made lowercase.
    claimstatus = models.TextField(db_column='CLAIMSTATUS', blank=True, null=True)  # Field name made lowercase.
    adjcode = models.TextField(db_column='ADJCODE', blank=True, null=True)  # Field name made lowercase.
    provid = models.IntegerField(db_column='PROVID', blank=True, null=True)  # Field name made lowercase.
    provname = models.TextField(db_column='PROVNAME', blank=True, null=True)  # Field name made lowercase.
    providerfirstname = models.TextField(db_column='PROVIDERFIRSTNAME', blank=True, null=True)  # Field name made lowercase.
    providerlastname = models.TextField(db_column='PROVIDERLASTNAME', blank=True, null=True)  # Field name made lowercase.
    provnpi = models.TextField(db_column='PROVNPI', blank=True, null=True)  # Field name made lowercase.
    provzipcode = models.TextField(db_column='PROVZIPCODE', blank=True, null=True)  # Field name made lowercase.
    servtypecode = models.IntegerField(db_column='SERVTYPECODE', blank=True, null=True)  # Field name made lowercase.
    servtypedesc = models.TextField(db_column='SERVTYPEDESC', blank=True, null=True)  # Field name made lowercase.
    provtypecode = models.TextField(db_column='PROVTYPECODE', blank=True, null=True)  # Field name made lowercase.
    provtypedesc = models.TextField(db_column='PROVTYPEDESC', blank=True, null=True)  # Field name made lowercase.
    servicecode = models.TextField(db_column='SERVICECODE', blank=True, null=True)  # Field name made lowercase.
    specrollupcode = models.TextField(db_column='SPECROLLUPCODE', blank=True, null=True)  # Field name made lowercase.
    specrollupdesc = models.TextField(db_column='SPECROLLUPDESC', blank=True, null=True)  # Field name made lowercase.
    nwkid = models.IntegerField(db_column='NWKID', blank=True, null=True)  # Field name made lowercase.
    nwkname = models.TextField(db_column='NWKNAME', blank=True, null=True)  # Field name made lowercase.
    innwk = models.TextField(db_column='INNWK', blank=True, null=True)  # Field name made lowercase.
    networktype = models.TextField(db_column='NETWORKTYPE', blank=True, null=True)  # Field name made lowercase.
    serviceunits = models.IntegerField(db_column='SERVICEUNITS', blank=True, null=True)  # Field name made lowercase.
    paidamt = models.IntegerField(db_column='PAIDAMT', blank=True, null=True)  # Field name made lowercase.
    billedamt = models.IntegerField(db_column='BILLEDAMT', blank=True, null=True)  # Field name made lowercase.
    allowedamt = models.IntegerField(db_column='ALLOWEDAMT', blank=True, null=True)  # Field name made lowercase.
    pposavingamt = models.IntegerField(db_column='PPOSAVINGAMT', blank=True, null=True)  # Field name made lowercase.
    enrpaidamt = models.IntegerField(db_column='ENRPAIDAMT', blank=True, null=True)  # Field name made lowercase.
    coinsamt = models.IntegerField(db_column='COINSAMT', blank=True, null=True)  # Field name made lowercase.
    copayamt = models.IntegerField(db_column='COPAYAMT', blank=True, null=True)  # Field name made lowercase.
    deductamt = models.IntegerField(db_column='DEDUCTAMT', blank=True, null=True)  # Field name made lowercase.
    notallowedamt = models.IntegerField(db_column='NOTALLOWEDAMT', blank=True, null=True)  # Field name made lowercase.
    cobamt = models.IntegerField(db_column='COBAMT', blank=True, null=True)  # Field name made lowercase.
    planexclamt = models.TextField(db_column='PLANEXCLAMT', blank=True, null=True)  # Field name made lowercase.
    labtestdata = models.TextField(db_column='LABTESTDATA', blank=True, null=True)  # Field name made lowercase.
    siccode = models.TextField(db_column='SICCODE', blank=True, null=True)  # Field name made lowercase.
    sicdesc = models.TextField(db_column='SICDESC', blank=True, null=True)  # Field name made lowercase.
    ssn = models.TextField(db_column='SSN', blank=True, null=True)  # Field name made lowercase.
    rcvmth = models.IntegerField(db_column='RCVMTH', blank=True, null=True)  # Field name made lowercase.
    srcfilename = models.TextField(db_column='SRCFILENAME', blank=True, null=True)  # Field name made lowercase.
    sourceform = models.TextField(db_column='SOURCEFORM', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.TextField(db_column='SOURCETYPE', blank=True, null=True)  # Field name made lowercase.
    udfm1 = models.TextField(db_column='UDFM1', blank=True, null=True)  # Field name made lowercase.
    udfm2 = models.TextField(db_column='UDFM2', blank=True, null=True)  # Field name made lowercase.
    udf1 = models.TextField(db_column='UDF1', blank=True, null=True)  # Field name made lowercase.
    udf2 = models.TextField(db_column='UDF2', blank=True, null=True)  # Field name made lowercase.
    udf3 = models.TextField(db_column='UDF3', blank=True, null=True)  # Field name made lowercase.
    udf4 = models.TextField(db_column='UDF4', blank=True, null=True)  # Field name made lowercase.
    udf5 = models.TextField(db_column='UDF5', blank=True, null=True)  # Field name made lowercase.
    udf6 = models.TextField(db_column='UDF6', blank=True, null=True)  # Field name made lowercase.
    udf7 = models.TextField(db_column='UDF7', blank=True, null=True)  # Field name made lowercase.
    udf8 = models.TextField(db_column='UDF8', blank=True, null=True)  # Field name made lowercase.
    udf9 = models.TextField(db_column='UDF9', blank=True, null=True)  # Field name made lowercase.
    udfc1 = models.TextField(db_column='UDFC1', blank=True, null=True)  # Field name made lowercase.
    udfc2 = models.TextField(db_column='UDFC2', blank=True, null=True)  # Field name made lowercase.
    udfc3 = models.TextField(db_column='UDFC3', blank=True, null=True)  # Field name made lowercase.
    udfc4 = models.TextField(db_column='UDFC4', blank=True, null=True)  # Field name made lowercase.
    udfc5 = models.TextField(db_column='UDFC5', blank=True, null=True)  # Field name made lowercase.
    udfc6 = models.TextField(db_column='UDFC6', blank=True, null=True)  # Field name made lowercase.
    udfc7 = models.TextField(db_column='UDFC7', blank=True, null=True)  # Field name made lowercase.
    udfc8 = models.TextField(db_column='UDFC8', blank=True, null=True)  # Field name made lowercase.
    udfc9 = models.TextField(db_column='UDFC9', blank=True, null=True)  # Field name made lowercase.
    udfc10 = models.TextField(db_column='UDFC10', blank=True, null=True)  # Field name made lowercase.
    udfc11 = models.TextField(db_column='UDFC11', blank=True, null=True)  # Field name made lowercase.
    udfc12 = models.TextField(db_column='UDFC12', blank=True, null=True)  # Field name made lowercase.
    udfc13 = models.TextField(db_column='UDFC13', blank=True, null=True)  # Field name made lowercase.
    udfc14 = models.TextField(db_column='UDFC14', blank=True, null=True)  # Field name made lowercase.
    udfc15 = models.TextField(db_column='UDFC15', blank=True, null=True)  # Field name made lowercase.
    udfc16 = models.TextField(db_column='UDFC16', blank=True, null=True)  # Field name made lowercase.
    udfc17 = models.TextField(db_column='UDFC17', blank=True, null=True)  # Field name made lowercase.
    udfc18 = models.TextField(db_column='UDFC18', blank=True, null=True)  # Field name made lowercase.
    udfc19 = models.TextField(db_column='UDFC19', blank=True, null=True)  # Field name made lowercase.
    udfc20 = models.TextField(db_column='UDFC20', blank=True, null=True)  # Field name made lowercase.
    udfd1 = models.TextField(db_column='UDFD1', blank=True, null=True)  # Field name made lowercase.
    udfd2 = models.TextField(db_column='UDFD2', blank=True, null=True)  # Field name made lowercase.
    udfd3 = models.TextField(db_column='UDFD3', blank=True, null=True)  # Field name made lowercase.
    udfd4 = models.TextField(db_column='UDFD4', blank=True, null=True)  # Field name made lowercase.
    udfd5 = models.TextField(db_column='UDFD5', blank=True, null=True)  # Field name made lowercase.
    udfn1 = models.TextField(db_column='UDFN1', blank=True, null=True)  # Field name made lowercase.
    udfn2 = models.TextField(db_column='UDFN2', blank=True, null=True)  # Field name made lowercase.
    udfn3 = models.IntegerField(db_column='UDFN3', blank=True, null=True)  # Field name made lowercase.
    udfn4 = models.IntegerField(db_column='UDFN4', blank=True, null=True)  # Field name made lowercase.
    udfn5 = models.IntegerField(db_column='UDFN5', blank=True, null=True)  # Field name made lowercase.
    udfn6 = models.IntegerField(db_column='UDFN6', blank=True, null=True)  # Field name made lowercase.
    udfn7 = models.IntegerField(db_column='UDFN7', blank=True, null=True)  # Field name made lowercase.
    udfn8 = models.IntegerField(db_column='UDFN8', blank=True, null=True)  # Field name made lowercase.
    udfn9 = models.IntegerField(db_column='UDFN9', blank=True, null=True)  # Field name made lowercase.
    udfn10 = models.IntegerField(db_column='UDFN10', blank=True, null=True)  # Field name made lowercase.
    udfn11 = models.IntegerField(db_column='UDFN11', blank=True, null=True)  # Field name made lowercase.
    udfn12 = models.IntegerField(db_column='UDFN12', blank=True, null=True)  # Field name made lowercase.
    udfn13 = models.IntegerField(db_column='UDFN13', blank=True, null=True)  # Field name made lowercase.
    udfn14 = models.IntegerField(db_column='UDFN14', blank=True, null=True)  # Field name made lowercase.
    udfn15 = models.IntegerField(db_column='UDFN15', blank=True, null=True)  # Field name made lowercase.
    udfn16 = models.IntegerField(db_column='UDFN16', blank=True, null=True)  # Field name made lowercase.
    udfn17 = models.IntegerField(db_column='UDFN17', blank=True, null=True)  # Field name made lowercase.
    udfn18 = models.IntegerField(db_column='UDFN18', blank=True, null=True)  # Field name made lowercase.
    udfn19 = models.IntegerField(db_column='UDFN19', blank=True, null=True)  # Field name made lowercase.
    udfn20 = models.IntegerField(db_column='UDFN20', blank=True, null=True)  # Field name made lowercase.
    vh_lvl_id = models.TextField(db_column='VH_LVL_ID', blank=True, null=True)  # Field name made lowercase.
    paiddays = models.TextField(db_column='PAIDDAYS', blank=True, null=True)  # Field name made lowercase.
    emp_nbr = models.TextField(db_column='EMP_NBR', blank=True, null=True)  # Field name made lowercase.
    medeligcatid = models.TextField(db_column='MEDELIGCATID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='PRODUCTID', blank=True, null=True)  # Field name made lowercase.
    icdtype = models.TextField(db_column='ICDTYPE', blank=True, null=True)  # Field name made lowercase.
    clmheadernumber = models.TextField(db_column='CLMHEADERNUMBER', blank=True, null=True)  # Field name made lowercase.
    vhpayorid = models.TextField(db_column='VHPAYORID', blank=True, null=True)  # Field name made lowercase.
    vhlayoutid = models.TextField(db_column='VHLAYOUTID', blank=True, null=True)  # Field name made lowercase.
    nchclmtypecode = models.IntegerField(db_column='NCHCLMTYPECODE', blank=True, null=True)  # Field name made lowercase.
    admittype = models.TextField(db_column='ADMITTYPE', blank=True, null=True)  # Field name made lowercase.
    admitsource = models.TextField(db_column='ADMITSOURCE', blank=True, null=True)  # Field name made lowercase.
    srcrelflag = models.TextField(db_column='SRCRELFLAG', blank=True, null=True)  # Field name made lowercase.
    mdcr_npmt_rsn_cd = models.TextField(db_column='MDCR_NPMT_RSN_CD', blank=True, null=True)  # Field name made lowercase.
    prov_ccn = models.TextField(db_column='PROV_CCN', blank=True, null=True)  # Field name made lowercase.
    clm_adjsmt_type_cd = models.TextField(db_column='CLM_ADJSMT_TYPE_CD', blank=True, null=True)  # Field name made lowercase.
    clm_query_cd = models.TextField(db_column='CLM_QUERY_CD', blank=True, null=True)  # Field name made lowercase.
    prncpl_diag_cd = models.TextField(db_column='PRNCPL_DIAG_CD', blank=True, null=True)  # Field name made lowercase.
    admtg_diag_cd = models.TextField(db_column='ADMTG_DIAG_CD', blank=True, null=True)  # Field name made lowercase.
    hdr_from_dt = models.TextField(db_column='HDR_FROM_DT', blank=True, null=True)  # Field name made lowercase.
    hdr_thru_dt = models.TextField(db_column='HDR_THRU_DT', blank=True, null=True)  # Field name made lowercase.
    op_srvc_typ_cd = models.TextField(db_column='OP_SRVC_TYP_CD', blank=True, null=True)  # Field name made lowercase.
    aifileid = models.TextField(db_column='AIFILEID', blank=True, null=True)  # Field name made lowercase.
    airownumber = models.TextField(db_column='AIROWNUMBER', blank=True, null=True)  # Field name made lowercase.
    vhpayername = models.TextField(db_column='VHPAYERNAME', blank=True, null=True)  # Field name made lowercase.
    vhgroupname = models.TextField(db_column='VHGROUPNAME', blank=True, null=True)  # Field name made lowercase.
    plannumber = models.TextField(db_column='PLANNUMBER', blank=True, null=True)  # Field name made lowercase.
    planname = models.TextField(db_column='PLANNAME', blank=True, null=True)  # Field name made lowercase.
    plantype = models.TextField(db_column='PLANTYPE', blank=True, null=True)  # Field name made lowercase.
    populationtype = models.TextField(db_column='POPULATIONTYPE', blank=True, null=True)  # Field name made lowercase.
    refrngprovid = models.TextField(db_column='REFRNGPROVID', blank=True, null=True)  # Field name made lowercase.
    refrngprovname = models.TextField(db_column='REFRNGPROVNAME', blank=True, null=True)  # Field name made lowercase.
    refrngprovnpi = models.TextField(db_column='REFRNGPROVNPI', blank=True, null=True)  # Field name made lowercase.
    billngprovid = models.TextField(db_column='BILLNGPROVID', blank=True, null=True)  # Field name made lowercase.
    billngprovname = models.TextField(db_column='BILLNGPROVNAME', blank=True, null=True)  # Field name made lowercase.
    billngprovnpi = models.TextField(db_column='BILLNGPROVNPI', blank=True, null=True)  # Field name made lowercase.
    billngprovtaxid = models.TextField(db_column='BILLNGPROVTAXID', blank=True, null=True)  # Field name made lowercase.
    srvcngprovid = models.TextField(db_column='SRVCNGPROVID', blank=True, null=True)  # Field name made lowercase.
    srvcngprovname = models.TextField(db_column='SRVCNGPROVNAME', blank=True, null=True)  # Field name made lowercase.
    srvcngprovnpi = models.TextField(db_column='SRVCNGPROVNPI', blank=True, null=True)  # Field name made lowercase.
    atndngprovid = models.TextField(db_column='ATNDNGPROVID', blank=True, null=True)  # Field name made lowercase.
    atndngprovname = models.TextField(db_column='ATNDNGPROVNAME', blank=True, null=True)  # Field name made lowercase.
    atndngprovnpi = models.TextField(db_column='ATNDNGPROVNPI', blank=True, null=True)  # Field name made lowercase.
    oprtngprovid = models.TextField(db_column='OPRTNGPROVID', blank=True, null=True)  # Field name made lowercase.
    oprtngprovname = models.TextField(db_column='OPRTNGPROVNAME', blank=True, null=True)  # Field name made lowercase.
    oprtngprovnpi = models.TextField(db_column='OPRTNGPROVNPI', blank=True, null=True)  # Field name made lowercase.
    otherprov1id = models.TextField(db_column='OTHERPROV1ID', blank=True, null=True)  # Field name made lowercase.
    otherprov1name = models.TextField(db_column='OTHERPROV1NAME', blank=True, null=True)  # Field name made lowercase.
    otherprov1npi = models.TextField(db_column='OTHERPROV1NPI', blank=True, null=True)  # Field name made lowercase.
    otherprov2id = models.TextField(db_column='OTHERPROV2ID', blank=True, null=True)  # Field name made lowercase.
    otherprov2name = models.TextField(db_column='OTHERPROV2NAME', blank=True, null=True)  # Field name made lowercase.
    otherprov2npi = models.TextField(db_column='OTHERPROV2NPI', blank=True, null=True)  # Field name made lowercase.
    payment_type_cd = models.TextField(db_column='PAYMENT_TYPE_CD', blank=True, null=True)  # Field name made lowercase.
    poa_firstdiagcode = models.IntegerField(db_column='POA_FIRSTDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_seconddiagcode = models.IntegerField(db_column='POA_SECONDDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_thirddiagcode = models.IntegerField(db_column='POA_THIRDDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_fourthdiagcode = models.IntegerField(db_column='POA_FOURTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_fifthdiagcode = models.IntegerField(db_column='POA_FIFTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_sixthdiagcode = models.IntegerField(db_column='POA_SIXTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_seventhdiagcode = models.IntegerField(db_column='POA_SEVENTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_eighthdiagcode = models.IntegerField(db_column='POA_EIGHTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_ninthdiagcode = models.IntegerField(db_column='POA_NINTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_tenthdiagcode = models.IntegerField(db_column='POA_TENTHDIAGCODE', blank=True, null=True)  # Field name made lowercase.
    poa_prncpl_diag_cd = models.IntegerField(db_column='POA_PRNCPL_DIAG_CD', blank=True, null=True)  # Field name made lowercase.
    poa_admtg_diag_cd = models.IntegerField(db_column='POA_ADMTG_DIAG_CD', blank=True, null=True)  # Field name made lowercase.
    i_src_orcl_row_id = models.TextField(db_column='I_SRC_ORCL_ROW_ID', blank=True, null=True)  # Field name made lowercase.
    i_src_tbl_nm = models.TextField(db_column='I_SRC_TBL_NM', blank=True, null=True)  # Field name made lowercase.
    adjflag = models.TextField(db_column='ADJFLAG', blank=True, null=True)  # Field name made lowercase.
    cmstatus = models.TextField(db_column='CMSTATUS', blank=True, null=True)  # Field name made lowercase.
    dischrgind = models.TextField(db_column='DISCHRGIND', blank=True, null=True)  # Field name made lowercase.
    dupcheck = models.TextField(db_column='DUPCHECK', blank=True, null=True)  # Field name made lowercase.
    fundcode = models.TextField(db_column='FUNDCODE', blank=True, null=True)  # Field name made lowercase.
    funddesc = models.TextField(db_column='FUNDDESC', blank=True, null=True)  # Field name made lowercase.
    grosscharge = models.IntegerField(db_column='GROSSCHARGE', blank=True, null=True)  # Field name made lowercase.
    iuou = models.TextField(db_column='IUOU', blank=True, null=True)  # Field name made lowercase.
    lvl4firstname = models.TextField(db_column='LVL4FIRSTNAME', blank=True, null=True)  # Field name made lowercase.
    lvl4lastname = models.TextField(db_column='LVL4LASTNAME', blank=True, null=True)  # Field name made lowercase.
    nwkcity = models.TextField(db_column='NWKCITY', blank=True, null=True)  # Field name made lowercase.
    nwkstate = models.TextField(db_column='NWKSTATE', blank=True, null=True)  # Field name made lowercase.
    ooa = models.TextField(db_column='OOA', blank=True, null=True)  # Field name made lowercase.
    persistencefactor = models.TextField(db_column='PERSISTENCEFACTOR', blank=True, null=True)  # Field name made lowercase.
    preferred = models.TextField(db_column='PREFERRED', blank=True, null=True)  # Field name made lowercase.
    provcity = models.TextField(db_column='PROVCITY', blank=True, null=True)  # Field name made lowercase.
    provpres_yn = models.TextField(db_column='PROVPRES_YN', blank=True, null=True)  # Field name made lowercase.
    provstate = models.TextField(db_column='PROVSTATE', blank=True, null=True)  # Field name made lowercase.
    reinsamt = models.IntegerField(db_column='REINSAMT', blank=True, null=True)  # Field name made lowercase.
    repricedamt = models.IntegerField(db_column='REPRICEDAMT', blank=True, null=True)  # Field name made lowercase.
    subscriberflag = models.TextField(db_column='SUBSCRIBERFLAG', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'testing_claims'


class TestingElig(models.Model):
    row_id = models.TextField(db_column='ROW_ID', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='SOURCE', blank=True, null=True)  # Field name made lowercase.
    memid = models.IntegerField(db_column='MEMID', blank=True, null=True)  # Field name made lowercase.
    enrid = models.IntegerField(db_column='ENRID', blank=True, null=True)  # Field name made lowercase.
    relflag = models.TextField(db_column='RELFLAG', blank=True, null=True)  # Field name made lowercase.
    memfirstname = models.TextField(db_column='MEMFIRSTNAME', blank=True, null=True)  # Field name made lowercase.
    memlastname = models.TextField(db_column='MEMLASTNAME', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    dob = models.TextField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    addr1 = models.TextField(db_column='ADDR1', blank=True, null=True)  # Field name made lowercase.
    addr2 = models.TextField(db_column='ADDR2', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    homephone = models.TextField(db_column='HOMEPHONE', blank=True, null=True)  # Field name made lowercase.
    workphone = models.TextField(db_column='WORKPHONE', blank=True, null=True)  # Field name made lowercase.
    covtypeid = models.TextField(db_column='COVTYPEID', blank=True, null=True)  # Field name made lowercase.
    covtypedesc = models.TextField(db_column='COVTYPEDESC', blank=True, null=True)  # Field name made lowercase.
    effdate = models.TextField(db_column='EFFDATE', blank=True, null=True)  # Field name made lowercase.
    termdate = models.TextField(db_column='TERMDATE', blank=True, null=True)  # Field name made lowercase.
    lvlid1 = models.TextField(db_column='LVLID1', blank=True, null=True)  # Field name made lowercase.
    lvldesc1 = models.TextField(db_column='LVLDESC1', blank=True, null=True)  # Field name made lowercase.
    lvlid2 = models.IntegerField(db_column='LVLID2', blank=True, null=True)  # Field name made lowercase.
    lvldesc2 = models.TextField(db_column='LVLDESC2', blank=True, null=True)  # Field name made lowercase.
    lvlid3 = models.TextField(db_column='LVLID3', blank=True, null=True)  # Field name made lowercase.
    lvldesc3 = models.TextField(db_column='LVLDESC3', blank=True, null=True)  # Field name made lowercase.
    lvlid4 = models.IntegerField(db_column='LVLID4', blank=True, null=True)  # Field name made lowercase.
    lvldesc4 = models.TextField(db_column='LVLDESC4', blank=True, null=True)  # Field name made lowercase.
    lvlid5 = models.TextField(db_column='LVLID5', blank=True, null=True)  # Field name made lowercase.
    lvldesc5 = models.TextField(db_column='LVLDESC5', blank=True, null=True)  # Field name made lowercase.
    lvlid6 = models.TextField(db_column='LVLID6', blank=True, null=True)  # Field name made lowercase.
    lvldesc6 = models.TextField(db_column='LVLDESC6', blank=True, null=True)  # Field name made lowercase.
    lvlid7 = models.TextField(db_column='LVLID7', blank=True, null=True)  # Field name made lowercase.
    lvldesc7 = models.TextField(db_column='LVLDESC7', blank=True, null=True)  # Field name made lowercase.
    lvlid8 = models.TextField(db_column='LVLID8', blank=True, null=True)  # Field name made lowercase.
    lvldesc8 = models.TextField(db_column='LVLDESC8', blank=True, null=True)  # Field name made lowercase.
    lvlid9 = models.TextField(db_column='LVLID9', blank=True, null=True)  # Field name made lowercase.
    lvldesc9 = models.TextField(db_column='LVLDESC9', blank=True, null=True)  # Field name made lowercase.
    lvlid10 = models.TextField(db_column='LVLID10', blank=True, null=True)  # Field name made lowercase.
    lvldesc10 = models.TextField(db_column='LVLDESC10', blank=True, null=True)  # Field name made lowercase.
    cmstatus = models.TextField(db_column='CMSTATUS', blank=True, null=True)  # Field name made lowercase.
    pcpid = models.TextField(db_column='PCPID', blank=True, null=True)  # Field name made lowercase.
    pcpname = models.TextField(db_column='PCPNAME', blank=True, null=True)  # Field name made lowercase.
    ssn = models.TextField(db_column='SSN', blank=True, null=True)  # Field name made lowercase.
    bencovtype = models.TextField(db_column='BENCOVTYPE', blank=True, null=True)  # Field name made lowercase.
    bencovtypedesc = models.TextField(db_column='BENCOVTYPEDESC', blank=True, null=True)  # Field name made lowercase.
    siccode = models.TextField(db_column='SICCODE', blank=True, null=True)  # Field name made lowercase.
    sicdesc = models.TextField(db_column='SICDESC', blank=True, null=True)  # Field name made lowercase.
    payertype = models.TextField(db_column='PAYERTYPE', blank=True, null=True)  # Field name made lowercase.
    rcvmth = models.IntegerField(db_column='RCVMTH', blank=True, null=True)  # Field name made lowercase.
    srcfilename = models.TextField(db_column='SRCFILENAME', blank=True, null=True)  # Field name made lowercase.
    udf1 = models.TextField(db_column='UDF1', blank=True, null=True)  # Field name made lowercase.
    udf1_mem = models.TextField(db_column='UDF1_MEM', blank=True, null=True)  # Field name made lowercase.
    udf2 = models.TextField(db_column='UDF2', blank=True, null=True)  # Field name made lowercase.
    udf2_mem = models.TextField(db_column='UDF2_MEM', blank=True, null=True)  # Field name made lowercase.
    udfc1 = models.TextField(db_column='UDFC1', blank=True, null=True)  # Field name made lowercase.
    udfc2 = models.TextField(db_column='UDFC2', blank=True, null=True)  # Field name made lowercase.
    udfc3 = models.TextField(db_column='UDFC3', blank=True, null=True)  # Field name made lowercase.
    udfc4 = models.TextField(db_column='UDFC4', blank=True, null=True)  # Field name made lowercase.
    udfc5 = models.TextField(db_column='UDFC5', blank=True, null=True)  # Field name made lowercase.
    udfc6 = models.TextField(db_column='UDFC6', blank=True, null=True)  # Field name made lowercase.
    udfc7 = models.TextField(db_column='UDFC7', blank=True, null=True)  # Field name made lowercase.
    udfc8 = models.TextField(db_column='UDFC8', blank=True, null=True)  # Field name made lowercase.
    udfc9 = models.TextField(db_column='UDFC9', blank=True, null=True)  # Field name made lowercase.
    udfc10 = models.TextField(db_column='UDFC10', blank=True, null=True)  # Field name made lowercase.
    udfc11 = models.TextField(db_column='UDFC11', blank=True, null=True)  # Field name made lowercase.
    udfc12 = models.TextField(db_column='UDFC12', blank=True, null=True)  # Field name made lowercase.
    udfc13 = models.TextField(db_column='UDFC13', blank=True, null=True)  # Field name made lowercase.
    udfc14 = models.TextField(db_column='UDFC14', blank=True, null=True)  # Field name made lowercase.
    udfc15 = models.TextField(db_column='UDFC15', blank=True, null=True)  # Field name made lowercase.
    udfc16 = models.TextField(db_column='UDFC16', blank=True, null=True)  # Field name made lowercase.
    udfc17 = models.TextField(db_column='UDFC17', blank=True, null=True)  # Field name made lowercase.
    udfc18 = models.TextField(db_column='UDFC18', blank=True, null=True)  # Field name made lowercase.
    udfc19 = models.TextField(db_column='UDFC19', blank=True, null=True)  # Field name made lowercase.
    udfc20 = models.TextField(db_column='UDFC20', blank=True, null=True)  # Field name made lowercase.
    udfd1 = models.TextField(db_column='UDFD1', blank=True, null=True)  # Field name made lowercase.
    udfd2 = models.TextField(db_column='UDFD2', blank=True, null=True)  # Field name made lowercase.
    udfd3 = models.TextField(db_column='UDFD3', blank=True, null=True)  # Field name made lowercase.
    udfd4 = models.TextField(db_column='UDFD4', blank=True, null=True)  # Field name made lowercase.
    udfn1 = models.TextField(db_column='UDFN1', blank=True, null=True)  # Field name made lowercase.
    udfn2 = models.TextField(db_column='UDFN2', blank=True, null=True)  # Field name made lowercase.
    vh_lvl_id = models.TextField(db_column='VH_LVL_ID', blank=True, null=True)  # Field name made lowercase.
    elig_begin_date = models.TextField(db_column='ELIG_BEGIN_DATE', blank=True, null=True)  # Field name made lowercase.
    elig_last_date = models.TextField(db_column='ELIG_LAST_DATE', blank=True, null=True)  # Field name made lowercase.
    begin_dte = models.TextField(db_column='BEGIN_DTE', blank=True, null=True)  # Field name made lowercase.
    end_dte = models.TextField(db_column='END_DTE', blank=True, null=True)  # Field name made lowercase.
    fom_dte = models.TextField(db_column='FOM_DTE', blank=True, null=True)  # Field name made lowercase.
    elig_flag = models.TextField(db_column='ELIG_FLAG', blank=True, null=True)  # Field name made lowercase.
    hpemployee = models.TextField(db_column='HPEMPLOYEE', blank=True, null=True)  # Field name made lowercase.
    emp_nbr = models.TextField(db_column='EMP_NBR', blank=True, null=True)  # Field name made lowercase.
    medeligcatid = models.TextField(db_column='MEDELIGCATID', blank=True, null=True)  # Field name made lowercase.
    productid = models.TextField(db_column='PRODUCTID', blank=True, null=True)  # Field name made lowercase.
    srcrelflag = models.TextField(db_column='SRCRELFLAG', blank=True, null=True)  # Field name made lowercase.
    coveragestatus = models.TextField(db_column='COVERAGESTATUS', blank=True, null=True)  # Field name made lowercase.
    plantype = models.TextField(db_column='PLANTYPE', blank=True, null=True)  # Field name made lowercase.
    planname = models.TextField(db_column='PLANNAME', blank=True, null=True)  # Field name made lowercase.
    vhpayorid = models.TextField(db_column='VHPAYORID', blank=True, null=True)  # Field name made lowercase.
    vhlayoutid = models.TextField(db_column='VHLAYOUTID', blank=True, null=True)  # Field name made lowercase.
    empstatuscode = models.TextField(db_column='EMPSTATUSCODE', blank=True, null=True)  # Field name made lowercase.
    empstatusdesc = models.TextField(db_column='EMPSTATUSDESC', blank=True, null=True)  # Field name made lowercase.
    mcaid1 = models.TextField(db_column='MCAID1', blank=True, null=True)  # Field name made lowercase.
    eligcat = models.TextField(db_column='ELIGCAT', blank=True, null=True)  # Field name made lowercase.
    orec = models.TextField(db_column='OREC', blank=True, null=True)  # Field name made lowercase.
    hospicecov = models.TextField(db_column='HOSPICECOV', blank=True, null=True)  # Field name made lowercase.
    product_id_2 = models.TextField(db_column='PRODUCT_ID_2', blank=True, null=True)  # Field name made lowercase.
    aifileid = models.TextField(db_column='AIFILEID', blank=True, null=True)  # Field name made lowercase.
    airownumber = models.TextField(db_column='AIROWNUMBER', blank=True, null=True)  # Field name made lowercase.
    vhpayername = models.TextField(db_column='VHPAYERNAME', blank=True, null=True)  # Field name made lowercase.
    vhgroupname = models.TextField(db_column='VHGROUPNAME', blank=True, null=True)  # Field name made lowercase.
    plannumber = models.TextField(db_column='PLANNUMBER', blank=True, null=True)  # Field name made lowercase.
    populationtype = models.TextField(db_column='POPULATIONTYPE', blank=True, null=True)  # Field name made lowercase.
    race_id = models.TextField(db_column='RACE_ID', blank=True, null=True)  # Field name made lowercase.
    dod = models.TextField(db_column='DOD', blank=True, null=True)  # Field name made lowercase.
    i_src_orcl_row_id = models.TextField(db_column='I_SRC_ORCL_ROW_ID', blank=True, null=True)  # Field name made lowercase.
    i_src_tbl_nm = models.TextField(db_column='I_SRC_TBL_NM', blank=True, null=True)  # Field name made lowercase.
    empzip = models.TextField(db_column='EMPZIP', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    lvl4firstname = models.TextField(db_column='LVL4FIRSTNAME', blank=True, null=True)  # Field name made lowercase.
    lvl4lastname = models.TextField(db_column='LVL4LASTNAME', blank=True, null=True)  # Field name made lowercase.
    subscriberflag = models.TextField(db_column='SUBSCRIBERFLAG', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'testing_elig'


class TestingRxclaims(models.Model):
    source = models.TextField(db_column='SOURCE', blank=True, null=True)  # Field name made lowercase.
    sn = models.IntegerField(db_column='SN', blank=True, null=True)  # Field name made lowercase.
    transnum = models.TextField(db_column='TRANSNUM', blank=True, null=True)  # Field name made lowercase.
    seqno = models.TextField(db_column='SEQNO', blank=True, null=True)  # Field name made lowercase.
    datetimestamp = models.TextField(db_column='DATETIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    memid = models.IntegerField(db_column='MEMID', blank=True, null=True)  # Field name made lowercase.
    enrid = models.IntegerField(db_column='ENRID', blank=True, null=True)  # Field name made lowercase.
    relflag = models.TextField(db_column='RELFLAG', blank=True, null=True)  # Field name made lowercase.
    memfirstname = models.TextField(db_column='MEMFIRSTNAME', blank=True, null=True)  # Field name made lowercase.
    memlastname = models.TextField(db_column='MEMLASTNAME', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    dob = models.TextField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    addr1 = models.TextField(db_column='ADDR1', blank=True, null=True)  # Field name made lowercase.
    addr2 = models.TextField(db_column='ADDR2', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    homephone = models.TextField(db_column='HOMEPHONE', blank=True, null=True)  # Field name made lowercase.
    workphone = models.TextField(db_column='WORKPHONE', blank=True, null=True)  # Field name made lowercase.
    lvlid1 = models.TextField(db_column='LVLID1', blank=True, null=True)  # Field name made lowercase.
    lvldesc1 = models.TextField(db_column='LVLDESC1', blank=True, null=True)  # Field name made lowercase.
    lvlid2 = models.IntegerField(db_column='LVLID2', blank=True, null=True)  # Field name made lowercase.
    lvldesc2 = models.TextField(db_column='LVLDESC2', blank=True, null=True)  # Field name made lowercase.
    lvlid3 = models.TextField(db_column='LVLID3', blank=True, null=True)  # Field name made lowercase.
    lvldesc3 = models.TextField(db_column='LVLDESC3', blank=True, null=True)  # Field name made lowercase.
    lvlid4 = models.IntegerField(db_column='LVLID4', blank=True, null=True)  # Field name made lowercase.
    lvldesc4 = models.TextField(db_column='LVLDESC4', blank=True, null=True)  # Field name made lowercase.
    lvlid5 = models.TextField(db_column='LVLID5', blank=True, null=True)  # Field name made lowercase.
    lvldesc5 = models.TextField(db_column='LVLDESC5', blank=True, null=True)  # Field name made lowercase.
    lvlid6 = models.TextField(db_column='LVLID6', blank=True, null=True)  # Field name made lowercase.
    lvldesc6 = models.TextField(db_column='LVLDESC6', blank=True, null=True)  # Field name made lowercase.
    lvlid7 = models.TextField(db_column='LVLID7', blank=True, null=True)  # Field name made lowercase.
    lvldesc7 = models.TextField(db_column='LVLDESC7', blank=True, null=True)  # Field name made lowercase.
    lvlid8 = models.TextField(db_column='LVLID8', blank=True, null=True)  # Field name made lowercase.
    lvldesc8 = models.TextField(db_column='LVLDESC8', blank=True, null=True)  # Field name made lowercase.
    lvlid9 = models.TextField(db_column='LVLID9', blank=True, null=True)  # Field name made lowercase.
    lvldesc9 = models.TextField(db_column='LVLDESC9', blank=True, null=True)  # Field name made lowercase.
    lvlid10 = models.TextField(db_column='LVLID10', blank=True, null=True)  # Field name made lowercase.
    lvldesc10 = models.TextField(db_column='LVLDESC10', blank=True, null=True)  # Field name made lowercase.
    filldate = models.TextField(db_column='FILLDATE', blank=True, null=True)  # Field name made lowercase.
    paiddate = models.TextField(db_column='PAIDDATE', blank=True, null=True)  # Field name made lowercase.
    metricquantity = models.IntegerField(db_column='METRICQUANTITY', blank=True, null=True)  # Field name made lowercase.
    dayssupply = models.IntegerField(db_column='DAYSSUPPLY', blank=True, null=True)  # Field name made lowercase.
    drugcode = models.IntegerField(db_column='DRUGCODE', blank=True, null=True)  # Field name made lowercase.
    drugdesc = models.TextField(db_column='DRUGDESC', blank=True, null=True)  # Field name made lowercase.
    drugstrength = models.TextField(db_column='DRUGSTRENGTH', blank=True, null=True)  # Field name made lowercase.
    formulary_yn = models.TextField(db_column='FORMULARY_YN', blank=True, null=True)  # Field name made lowercase.
    moi = models.TextField(db_column='MOI', blank=True, null=True)  # Field name made lowercase.
    prescriberid = models.IntegerField(db_column='PRESCRIBERID', blank=True, null=True)  # Field name made lowercase.
    prescribertype = models.TextField(db_column='PRESCRIBERTYPE', blank=True, null=True)  # Field name made lowercase.
    prescribername = models.TextField(db_column='PRESCRIBERNAME', blank=True, null=True)  # Field name made lowercase.
    pharmid = models.IntegerField(db_column='PHARMID', blank=True, null=True)  # Field name made lowercase.
    pharmname = models.TextField(db_column='PHARMNAME', blank=True, null=True)  # Field name made lowercase.
    pharmzipcode = models.TextField(db_column='PHARMZIPCODE', blank=True, null=True)  # Field name made lowercase.
    paidamt = models.FloatField(db_column='PAIDAMT', blank=True, null=True)  # Field name made lowercase.
    billedamt = models.FloatField(db_column='BILLEDAMT', blank=True, null=True)  # Field name made lowercase.
    ingredcost = models.IntegerField(db_column='INGREDCOST', blank=True, null=True)  # Field name made lowercase.
    dispensingcost = models.IntegerField(db_column='DISPENSINGCOST', blank=True, null=True)  # Field name made lowercase.
    salestax = models.IntegerField(db_column='SALESTAX', blank=True, null=True)  # Field name made lowercase.
    allowedamt = models.FloatField(db_column='ALLOWEDAMT', blank=True, null=True)  # Field name made lowercase.
    enrpaidamt = models.FloatField(db_column='ENRPAIDAMT', blank=True, null=True)  # Field name made lowercase.
    coinsamt = models.IntegerField(db_column='COINSAMT', blank=True, null=True)  # Field name made lowercase.
    copayamt = models.FloatField(db_column='COPAYAMT', blank=True, null=True)  # Field name made lowercase.
    deductamt = models.IntegerField(db_column='DEDUCTAMT', blank=True, null=True)  # Field name made lowercase.
    notallowedamt = models.IntegerField(db_column='NOTALLOWEDAMT', blank=True, null=True)  # Field name made lowercase.
    admfees = models.TextField(db_column='ADMFEES', blank=True, null=True)  # Field name made lowercase.
    awp = models.IntegerField(db_column='AWP', blank=True, null=True)  # Field name made lowercase.
    cobamt = models.IntegerField(db_column='COBAMT', blank=True, null=True)  # Field name made lowercase.
    adjcode = models.TextField(db_column='ADJCODE', blank=True, null=True)  # Field name made lowercase.
    siccode = models.TextField(db_column='SICCODE', blank=True, null=True)  # Field name made lowercase.
    sicdesc = models.TextField(db_column='SICDESC', blank=True, null=True)  # Field name made lowercase.
    claimstatus = models.TextField(db_column='CLAIMSTATUS', blank=True, null=True)  # Field name made lowercase.
    supplyflag = models.TextField(db_column='SUPPLYFLAG', blank=True, null=True)  # Field name made lowercase.
    discountamt = models.IntegerField(db_column='DISCOUNTAMT', blank=True, null=True)  # Field name made lowercase.
    prescount = models.TextField(db_column='PRESCOUNT', blank=True, null=True)  # Field name made lowercase.
    ssn = models.TextField(db_column='SSN', blank=True, null=True)  # Field name made lowercase.
    rcvmth = models.IntegerField(db_column='RCVMTH', blank=True, null=True)  # Field name made lowercase.
    srcfilename = models.TextField(db_column='SRCFILENAME', blank=True, null=True)  # Field name made lowercase.
    udf1 = models.TextField(db_column='UDF1', blank=True, null=True)  # Field name made lowercase.
    udfm1 = models.TextField(db_column='UDFM1', blank=True, null=True)  # Field name made lowercase.
    udf2 = models.TextField(db_column='UDF2', blank=True, null=True)  # Field name made lowercase.
    udfm2 = models.TextField(db_column='UDFM2', blank=True, null=True)  # Field name made lowercase.
    udf3 = models.TextField(db_column='UDF3', blank=True, null=True)  # Field name made lowercase.
    udf4 = models.TextField(db_column='UDF4', blank=True, null=True)  # Field name made lowercase.
    udf5 = models.TextField(db_column='UDF5', blank=True, null=True)  # Field name made lowercase.
    udf6 = models.TextField(db_column='UDF6', blank=True, null=True)  # Field name made lowercase.
    udf7 = models.TextField(db_column='UDF7', blank=True, null=True)  # Field name made lowercase.
    udf8 = models.TextField(db_column='UDF8', blank=True, null=True)  # Field name made lowercase.
    udf9 = models.TextField(db_column='UDF9', blank=True, null=True)  # Field name made lowercase.
    udfc1 = models.TextField(db_column='UDFC1', blank=True, null=True)  # Field name made lowercase.
    udfc2 = models.TextField(db_column='UDFC2', blank=True, null=True)  # Field name made lowercase.
    udfc3 = models.TextField(db_column='UDFC3', blank=True, null=True)  # Field name made lowercase.
    udfc4 = models.TextField(db_column='UDFC4', blank=True, null=True)  # Field name made lowercase.
    udfc5 = models.TextField(db_column='UDFC5', blank=True, null=True)  # Field name made lowercase.
    udfc6 = models.TextField(db_column='UDFC6', blank=True, null=True)  # Field name made lowercase.
    udfc7 = models.TextField(db_column='UDFC7', blank=True, null=True)  # Field name made lowercase.
    udfc8 = models.TextField(db_column='UDFC8', blank=True, null=True)  # Field name made lowercase.
    udfc9 = models.TextField(db_column='UDFC9', blank=True, null=True)  # Field name made lowercase.
    udfc10 = models.TextField(db_column='UDFC10', blank=True, null=True)  # Field name made lowercase.
    udfc11 = models.TextField(db_column='UDFC11', blank=True, null=True)  # Field name made lowercase.
    udfc12 = models.TextField(db_column='UDFC12', blank=True, null=True)  # Field name made lowercase.
    udfc13 = models.TextField(db_column='UDFC13', blank=True, null=True)  # Field name made lowercase.
    udfc14 = models.TextField(db_column='UDFC14', blank=True, null=True)  # Field name made lowercase.
    udfc15 = models.TextField(db_column='UDFC15', blank=True, null=True)  # Field name made lowercase.
    udfc16 = models.TextField(db_column='UDFC16', blank=True, null=True)  # Field name made lowercase.
    udfc17 = models.TextField(db_column='UDFC17', blank=True, null=True)  # Field name made lowercase.
    udfc18 = models.TextField(db_column='UDFC18', blank=True, null=True)  # Field name made lowercase.
    udfc19 = models.TextField(db_column='UDFC19', blank=True, null=True)  # Field name made lowercase.
    udfc20 = models.TextField(db_column='UDFC20', blank=True, null=True)  # Field name made lowercase.
    udfd1 = models.TextField(db_column='UDFD1', blank=True, null=True)  # Field name made lowercase.
    udfd2 = models.TextField(db_column='UDFD2', blank=True, null=True)  # Field name made lowercase.
    udfd3 = models.TextField(db_column='UDFD3', blank=True, null=True)  # Field name made lowercase.
    udfd4 = models.TextField(db_column='UDFD4', blank=True, null=True)  # Field name made lowercase.
    udfd5 = models.TextField(db_column='UDFD5', blank=True, null=True)  # Field name made lowercase.
    udfn1 = models.IntegerField(db_column='UDFN1', blank=True, null=True)  # Field name made lowercase.
    udfn2 = models.IntegerField(db_column='UDFN2', blank=True, null=True)  # Field name made lowercase.
    udfn3 = models.IntegerField(db_column='UDFN3', blank=True, null=True)  # Field name made lowercase.
    udfn4 = models.IntegerField(db_column='UDFN4', blank=True, null=True)  # Field name made lowercase.
    udfn5 = models.IntegerField(db_column='UDFN5', blank=True, null=True)  # Field name made lowercase.
    udfn6 = models.IntegerField(db_column='UDFN6', blank=True, null=True)  # Field name made lowercase.
    udfn7 = models.IntegerField(db_column='UDFN7', blank=True, null=True)  # Field name made lowercase.
    udfn8 = models.IntegerField(db_column='UDFN8', blank=True, null=True)  # Field name made lowercase.
    udfn9 = models.IntegerField(db_column='UDFN9', blank=True, null=True)  # Field name made lowercase.
    udfn10 = models.IntegerField(db_column='UDFN10', blank=True, null=True)  # Field name made lowercase.
    udfn11 = models.IntegerField(db_column='UDFN11', blank=True, null=True)  # Field name made lowercase.
    udfn12 = models.IntegerField(db_column='UDFN12', blank=True, null=True)  # Field name made lowercase.
    udfn13 = models.IntegerField(db_column='UDFN13', blank=True, null=True)  # Field name made lowercase.
    udfn14 = models.IntegerField(db_column='UDFN14', blank=True, null=True)  # Field name made lowercase.
    udfn15 = models.IntegerField(db_column='UDFN15', blank=True, null=True)  # Field name made lowercase.
    udfn16 = models.IntegerField(db_column='UDFN16', blank=True, null=True)  # Field name made lowercase.
    udfn17 = models.IntegerField(db_column='UDFN17', blank=True, null=True)  # Field name made lowercase.
    udfn18 = models.IntegerField(db_column='UDFN18', blank=True, null=True)  # Field name made lowercase.
    udfn19 = models.IntegerField(db_column='UDFN19', blank=True, null=True)  # Field name made lowercase.
    udfn20 = models.IntegerField(db_column='UDFN20', blank=True, null=True)  # Field name made lowercase.
    vh_lvl_id = models.TextField(db_column='VH_LVL_ID', blank=True, null=True)  # Field name made lowercase.
    emp_nbr = models.TextField(db_column='EMP_NBR', blank=True, null=True)  # Field name made lowercase.
    medeligcatid = models.TextField(db_column='MEDELIGCATID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='PRODUCTID', blank=True, null=True)  # Field name made lowercase.
    vhpayorid = models.TextField(db_column='VHPAYORID', blank=True, null=True)  # Field name made lowercase.
    vhlayoutid = models.TextField(db_column='VHLAYOUTID', blank=True, null=True)  # Field name made lowercase.
    qty_disp = models.TextField(db_column='QTY_DISP', blank=True, null=True)  # Field name made lowercase.
    srcrelflag = models.TextField(db_column='SRCRELFLAG', blank=True, null=True)  # Field name made lowercase.
    aifileid = models.TextField(db_column='AIFILEID', blank=True, null=True)  # Field name made lowercase.
    airownumber = models.TextField(db_column='AIROWNUMBER', blank=True, null=True)  # Field name made lowercase.
    vhpayername = models.TextField(db_column='VHPAYERNAME', blank=True, null=True)  # Field name made lowercase.
    vhgroupname = models.TextField(db_column='VHGROUPNAME', blank=True, null=True)  # Field name made lowercase.
    compoundind = models.TextField(db_column='COMPOUNDIND', blank=True, null=True)  # Field name made lowercase.
    specialtyind = models.TextField(db_column='SPECIALTYIND', blank=True, null=True)  # Field name made lowercase.
    pharmnabpnum = models.TextField(db_column='PHARMNABPNUM', blank=True, null=True)  # Field name made lowercase.
    plannumber = models.TextField(db_column='PLANNUMBER', blank=True, null=True)  # Field name made lowercase.
    planname = models.TextField(db_column='PLANNAME', blank=True, null=True)  # Field name made lowercase.
    plantype = models.TextField(db_column='PLANTYPE', blank=True, null=True)  # Field name made lowercase.
    populationtype = models.TextField(db_column='POPULATIONTYPE', blank=True, null=True)  # Field name made lowercase.
    i_src_orcl_row_id = models.TextField(db_column='I_SRC_ORCL_ROW_ID', blank=True, null=True)  # Field name made lowercase.
    i_src_tbl_nm = models.TextField(db_column='I_SRC_TBL_NM', blank=True, null=True)  # Field name made lowercase.
    dawps_cd = models.TextField(db_column='DAWPS_CD', blank=True, null=True)  # Field name made lowercase.
    rx_orgn_cd = models.TextField(db_column='RX_ORGN_CD', blank=True, null=True)  # Field name made lowercase.
    unc_price = models.TextField(db_column='UNC_PRICE', blank=True, null=True)  # Field name made lowercase.
    subscriberflag = models.TextField(db_column='SUBSCRIBERFLAG', blank=True, null=True)  # Field name made lowercase.
    lvl4firstname = models.TextField(db_column='LVL4FIRSTNAME', blank=True, null=True)  # Field name made lowercase.
    lvl4lastname = models.TextField(db_column='LVL4LASTNAME', blank=True, null=True)  # Field name made lowercase.
    cmstatus = models.TextField(db_column='CMSTATUS', blank=True, null=True)  # Field name made lowercase.
    drugtypecode = models.TextField(db_column='DRUGTYPECODE', blank=True, null=True)  # Field name made lowercase.
    drugtypedesc = models.TextField(db_column='DRUGTYPEDESC', blank=True, null=True)  # Field name made lowercase.
    gcn = models.TextField(db_column='GCN', blank=True, null=True)  # Field name made lowercase.
    gi = models.TextField(db_column='GI', blank=True, null=True)  # Field name made lowercase.
    gpi = models.TextField(db_column='GPI', blank=True, null=True)  # Field name made lowercase.
    rxcode = models.TextField(db_column='RXCODE', blank=True, null=True)  # Field name made lowercase.
    rxdesc = models.TextField(db_column='RXDESC', blank=True, null=True)  # Field name made lowercase.
    reinsamt = models.IntegerField(db_column='REINSAMT', blank=True, null=True)  # Field name made lowercase.
    repricedamt = models.IntegerField(db_column='REPRICEDAMT', blank=True, null=True)  # Field name made lowercase.
    persistencefactor = models.TextField(db_column='PERSISTENCEFACTOR', blank=True, null=True)  # Field name made lowercase.
    networktype = models.TextField(db_column='NETWORKTYPE', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'testing_rxclaims'

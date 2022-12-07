/*
   This file has been generated by IDA.
   It contains local type definitions from
   the type library 't8.exe'
*/

#define __int8 char
#define __int16 short
#define __int32 int
#define __int64 long long

struct _EXCEPTION_RECORD;
struct _CONTEXT;
union _LARGE_INTEGER;
struct _Mbstatet;
struct _s_ThrowInfo;
struct _s_CatchableTypeArray;
struct _s_CatchableType;
struct TypeDescriptor;
struct _RTL_CRITICAL_SECTION_DEBUG;

/* 1 */
enum __TI_flags
{
  TI_IsConst = 0x1,
  TI_IsVolatile = 0x2,
  TI_IsUnaligned = 0x4,
  TI_IsPure = 0x8,
  TI_IsWinRT = 0x10,
};

/* 2 */
enum __CT_flags
{
  CT_IsSimpleType = 0x1,
  CT_ByReferenceOnly = 0x2,
  CT_HasVirtualBase = 0x4,
  CT_IsWinRTHandle = 0x8,
  CT_IsStdBadAlloc = 0x10,
};

/* 3 */
struct _EH4_SCOPETABLE_RECORD
{
  int EnclosingLevel;
  void *FilterFunc;
  void *HandlerFunc;
};

/* 17 */
typedef unsigned int DWORD;

/* 4 */
struct _EH4_SCOPETABLE
{
  DWORD GSCookieOffset;
  DWORD GSCookieXOROffset;
  DWORD EHCookieOffset;
  DWORD EHCookieXOROffset;
  struct _EH4_SCOPETABLE_RECORD ScopeRecord[];
};

/* 5 */
typedef struct _SCOPETABLE_ENTRY *PSCOPETABLE_ENTRY;

/* 18 */
typedef void *PVOID;

/* 6 */
struct _EH3_EXCEPTION_REGISTRATION
{
  struct _EH3_EXCEPTION_REGISTRATION *Next;
  PVOID ExceptionHandler;
  PSCOPETABLE_ENTRY ScopeTable;
  DWORD TryLevel;
};

/* 7 */
typedef struct _EH3_EXCEPTION_REGISTRATION EH3_EXCEPTION_REGISTRATION;

/* 8 */
typedef struct _EH3_EXCEPTION_REGISTRATION *PEH3_EXCEPTION_REGISTRATION;

/* 9 */
struct CPPEH_RECORD
{
  DWORD old_esp;
  EXCEPTION_POINTERS *exc_ptr;
  struct _EH3_EXCEPTION_REGISTRATION registration;
};

/* 11 */
typedef unsigned int UINT;

/* 12 */
typedef unsigned __int8 BYTE;

/* 10 */
struct _cpinfo
{
  UINT MaxCharSize;
  BYTE DefaultChar[2];
  BYTE LeadByte[12];
};

/* 15 */
typedef _EXCEPTION_RECORD EXCEPTION_RECORD;

/* 14 */
typedef EXCEPTION_RECORD *PEXCEPTION_RECORD;

/* 21 */
typedef _CONTEXT CONTEXT;

/* 20 */
typedef CONTEXT *PCONTEXT;

/* 13 */
struct _EXCEPTION_POINTERS
{
  PEXCEPTION_RECORD ExceptionRecord;
  PCONTEXT ContextRecord;
};

/* 19 */
typedef unsigned int ULONG_PTR;

/* 16 */
struct _EXCEPTION_RECORD
{
  DWORD ExceptionCode;
  DWORD ExceptionFlags;
  _EXCEPTION_RECORD *ExceptionRecord;
  PVOID ExceptionAddress;
  DWORD NumberParameters;
  ULONG_PTR ExceptionInformation[15];
};

/* 24 */
struct _FLOATING_SAVE_AREA
{
  DWORD ControlWord;
  DWORD StatusWord;
  DWORD TagWord;
  DWORD ErrorOffset;
  DWORD ErrorSelector;
  DWORD DataOffset;
  DWORD DataSelector;
  BYTE RegisterArea[80];
  DWORD Spare0;
};

/* 23 */
typedef _FLOATING_SAVE_AREA FLOATING_SAVE_AREA;

/* 22 */
#pragma pack(push, 4)
struct _CONTEXT
{
  DWORD ContextFlags;
  DWORD Dr0;
  DWORD Dr1;
  DWORD Dr2;
  DWORD Dr3;
  DWORD Dr6;
  DWORD Dr7;
  FLOATING_SAVE_AREA FloatSave;
  DWORD SegGs;
  DWORD SegFs;
  DWORD SegEs;
  DWORD SegDs;
  DWORD Edi;
  DWORD Esi;
  DWORD Ebx;
  DWORD Edx;
  DWORD Ecx;
  DWORD Eax;
  DWORD Ebp;
  DWORD Eip;
  DWORD SegCs;
  DWORD EFlags;
  DWORD Esp;
  DWORD SegSs;
  BYTE ExtendedRegisters[512];
};
#pragma pack(pop)

/* 25 */
struct _FILETIME
{
  DWORD dwLowDateTime;
  DWORD dwHighDateTime;
};

/* 26 */
typedef _LARGE_INTEGER LARGE_INTEGER;

/* 29 */
typedef int LONG;

/* 28 */
struct _LARGE_INTEGER::$837407842DC9087486FDFA5FEB63B74E
{
  DWORD LowPart;
  LONG HighPart;
};

/* 30 */
typedef __int64 LONGLONG;

/* 27 */
union _LARGE_INTEGER
{
  struct
  {
    DWORD LowPart;
    LONG HighPart;
  };
  _LARGE_INTEGER::$837407842DC9087486FDFA5FEB63B74E u;
  LONGLONG QuadPart;
};

/* 33 */
typedef unsigned __int16 wchar_t;

/* 32 */
typedef wchar_t WCHAR;

/* 36 */
typedef unsigned __int16 WORD;

/* 35 */
struct _SYSTEMTIME
{
  WORD wYear;
  WORD wMonth;
  WORD wDayOfWeek;
  WORD wDay;
  WORD wHour;
  WORD wMinute;
  WORD wSecond;
  WORD wMilliseconds;
};

/* 34 */
typedef _SYSTEMTIME SYSTEMTIME;

/* 31 */
struct _TIME_ZONE_INFORMATION
{
  LONG Bias;
  WCHAR StandardName[32];
  SYSTEMTIME StandardDate;
  LONG StandardBias;
  WCHAR DaylightName[32];
  SYSTEMTIME DaylightDate;
  LONG DaylightBias;
};

/* 38 */
enum _FINDEX_INFO_LEVELS
{
  FindExInfoStandard = 0x0,
  FindExInfoBasic = 0x1,
  FindExInfoMaxInfoLevel = 0x2,
};

/* 37 */
typedef _FINDEX_INFO_LEVELS FINDEX_INFO_LEVELS;

/* 40 */
enum _FINDEX_SEARCH_OPS
{
  FindExSearchNameMatch = 0x0,
  FindExSearchLimitToDirectories = 0x1,
  FindExSearchLimitToDevices = 0x2,
  FindExSearchMaxSearchOp = 0x3,
};

/* 39 */
typedef _FINDEX_SEARCH_OPS FINDEX_SEARCH_OPS;

/* 42 */
typedef _FILETIME FILETIME;

/* 41 */
struct _WIN32_FIND_DATAW
{
  DWORD dwFileAttributes;
  FILETIME ftCreationTime;
  FILETIME ftLastAccessTime;
  FILETIME ftLastWriteTime;
  DWORD nFileSizeHigh;
  DWORD nFileSizeLow;
  DWORD dwReserved0;
  DWORD dwReserved1;
  WCHAR cFileName[260];
  WCHAR cAlternateFileName[14];
};

/* 43 */
typedef _Mbstatet mbstate_t;

/* 44 */
#pragma pack(push, 8)
struct _Mbstatet
{
  unsigned int _Wchar;
  unsigned __int16 _Byte;
  unsigned __int16 _State;
};
#pragma pack(pop)

/* 45 */
struct _Cvtvec
{
  unsigned int _Page;
  unsigned int _Mbcurmax;
  int _Isclocale;
  unsigned __int8 _Isleadbyte[32];
};

/* 46 */
struct _Ctypevec
{
  unsigned int _Page;
  const __int16 *_Table;
  int _Delfl;
  wchar_t *_LocaleName;
};

/* 48 */
typedef unsigned __int64 ULONGLONG;

/* 51 */
struct _SINGLE_LIST_ENTRY
{
  _SINGLE_LIST_ENTRY *Next;
};

/* 50 */
typedef _SINGLE_LIST_ENTRY SLIST_ENTRY;

/* 49 */
struct _SLIST_HEADER::$04C3B4B3818F1694974352AE64BF5082
{
  SLIST_ENTRY Next;
  WORD Depth;
  WORD CpuId;
};

/* 47 */
union _SLIST_HEADER
{
  ULONGLONG Alignment;
  struct
  {
    SLIST_ENTRY Next;
    WORD Depth;
    WORD CpuId;
  };
};

/* 52 */
struct FuncInfo
{
  int magicNumber;
  int maxState;
  void *pUnwindMap;
  int nTryBlocks;
  void *pTryBlockMap;
  int nIPMapEntries;
  void *pIPtoStateMap;
  void *pESTypeList;
  int EHFlags;
};

/* 53 */
struct UnwindMapEntry
{
  int toState;
  void *action;
};

/* 55 */
typedef const _s_ThrowInfo ThrowInfo;

/* 54 */
typedef ThrowInfo _ThrowInfo;

/* 57 */
typedef void (__cdecl *PMFN)(void *);

/* 58 */
typedef const _s_CatchableTypeArray CatchableTypeArray;

/* 56 */
#pragma pack(push, 4)
struct _s_ThrowInfo
{
  unsigned int attributes;
  PMFN pmfnUnwind;
  int (__cdecl *pForwardCompat)();
  CatchableTypeArray *pCatchableTypeArray;
};
#pragma pack(pop)

/* 60 */
typedef const _s_CatchableType CatchableType;

/* 59 */
#pragma pack(push, 4)
struct _s_CatchableTypeArray
{
  int nCatchableTypes;
  CatchableType *arrayOfCatchableTypes[];
};
#pragma pack(pop)

/* 63 */
#pragma pack(push, 4)
struct PMD
{
  int mdisp;
  int pdisp;
  int vdisp;
};
#pragma pack(pop)

/* 61 */
#pragma pack(push, 4)
struct _s_CatchableType
{
  unsigned int properties;
  TypeDescriptor *pType;
  PMD thisDisplacement;
  int sizeOrOffset;
  PMFN copyFunction;
};
#pragma pack(pop)

/* 62 */
#pragma pack(push, 4)
struct TypeDescriptor
{
  unsigned int hash;
  void *spare;
  char name[];
};
#pragma pack(pop)

/* 64 */
#pragma pack(push, 8)
struct __crt_locale_pointers
{
  struct __crt_locale_data *locinfo;
  struct __crt_multibyte_data *mbcinfo;
};
#pragma pack(pop)

/* 65 */
struct TryBlockMapEntry
{
  int tryLow;
  int tryHigh;
  int catchHigh;
  int nCatches;
  void *pHandlerArray;
};

/* 66 */
struct HandlerType
{
  int adjectives;
  void *pType;
  int dispCatchObj;
  void *addressOfHandler;
};

/* 67 */
enum _crt_argv_mode
{
  _crt_argv_no_arguments = 0x0,
  _crt_argv_unexpanded_arguments = 0x1,
  _crt_argv_expanded_arguments = 0x2,
};

/* 69 */
typedef void (__cdecl *_PVFV)();

/* 68 */
#pragma pack(push, 8)
struct _onexit_table_t
{
  _PVFV *_first;
  _PVFV *_last;
  _PVFV *_end;
};
#pragma pack(pop)

/* 71 */
typedef WCHAR *LPWSTR;

/* 72 */
typedef BYTE *LPBYTE;

/* 73 */
typedef void *HANDLE;

/* 70 */
struct _STARTUPINFOW
{
  DWORD cb;
  LPWSTR lpReserved;
  LPWSTR lpDesktop;
  LPWSTR lpTitle;
  DWORD dwX;
  DWORD dwY;
  DWORD dwXSize;
  DWORD dwYSize;
  DWORD dwXCountChars;
  DWORD dwYCountChars;
  DWORD dwFillAttribute;
  DWORD dwFlags;
  WORD wShowWindow;
  WORD cbReserved2;
  LPBYTE lpReserved2;
  HANDLE hStdInput;
  HANDLE hStdOutput;
  HANDLE hStdError;
};

/* 74 */
#pragma pack(push, 8)
struct fenv_t
{
  unsigned int _Fe_ctl;
  unsigned int _Fe_stat;
};
#pragma pack(pop)

/* 75 */
struct std::locale;

/* 76 */
struct std::locale::_Locimp;

/* 78 */
typedef _RTL_CRITICAL_SECTION_DEBUG *PRTL_CRITICAL_SECTION_DEBUG;

/* 77 */
#pragma pack(push, 8)
struct _RTL_CRITICAL_SECTION
{
  PRTL_CRITICAL_SECTION_DEBUG DebugInfo;
  LONG LockCount;
  LONG RecursionCount;
  HANDLE OwningThread;
  HANDLE LockSemaphore;
  ULONG_PTR SpinCount;
};
#pragma pack(pop)

/* 81 */
struct _LIST_ENTRY
{
  _LIST_ENTRY *Flink;
  _LIST_ENTRY *Blink;
};

/* 80 */
typedef _LIST_ENTRY LIST_ENTRY;

/* 79 */
struct _RTL_CRITICAL_SECTION_DEBUG
{
  WORD Type;
  WORD CreatorBackTraceIndex;
  _RTL_CRITICAL_SECTION *CriticalSection;
  LIST_ENTRY ProcessLocksList;
  DWORD EntryCount;
  DWORD ContentionCount;
  DWORD Flags;
  WORD CreatorBackTraceIndexHigh;
  WORD SpareWORD;
};

/* 82 */
struct std::_Locinfo;

/* 83 */
struct _LocaleUpdate;

/* 84 */
struct __crt_stdio_output::formatting_buffer;

/* 85 */
struct __crt_stdio_output;

/* 86 */
struct __crt_strtox::floating_point_value;

/* 87 */
struct __crt_strtox;

/* 88 */
struct __crt_mbstring;

/* 89 */
struct std::_Lockit;

/* 90 */
struct std::_Fac_node;

/* 91 */
struct std::_Fac_tidy_reg_t;

/* 92 */
struct _Init_atexit;

/* 93 */
struct std::_Init_locks;

/* 95 */
typedef int __ehstate_t;

/* 94 */
#pragma pack(push, 4)
struct EHRegistrationNode
{
  EHRegistrationNode *pNext;
  void *frameHandler;
  __ehstate_t state;
};
#pragma pack(pop)

/* 96 */
enum _crt_exit_cleanup_mode
{
  _crt_exit_full_cleanup = 0x0,
  _crt_exit_quick_cleanup = 0x1,
  _crt_exit_no_cleanup = 0x2,
};

/* 97 */
enum _crt_exit_return_mode
{
  _crt_exit_terminate_process = 0x0,
  _crt_exit_return_to_caller = 0x1,
};


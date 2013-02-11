class Project < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :project_users
  has_and_belongs_to_many :users
  has_many :tickets, :dependent => :destroy

  validates :name,
            :presence => true,
            :uniqueness => true,
            :length => { :in => 3..20, :allow_blank => true }
         
  validates_presence_of :description, :start_date, :end_date

  validate :validate_end_date_before_start_date

  
  def project_users=(project_users)
    # empty. defines attribute :project_users for join table
  end

  def validate_end_date_before_start_date
    if end_date && start_date
      errors.add(:end_date, "must be greater than start date.") if end_date <= start_date
    end
  end

end
